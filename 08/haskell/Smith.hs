module Smith
    ( smithFactors
    , matrixRank
    ) where

-- | Integer matrix as list of rows.
type Matrix = [[Int]]

-- | Compute the nonzero invariant factors of an integer matrix.
--
--   Uses the Euclidean algorithm extended to matrices (Hermite/Smith reduction).
--   The result is a list [d_1, ..., d_r] of positive integers with d_i | d_{i+1}.
--   The rank of the matrix is r = length of the result.
smithFactors :: Matrix -> [Int]
smithFactors [] = []
smithFactors ([]:_) = []
smithFactors m = go (map (map id) m) 0
  where
    nrows = length m
    ncols = if null m then 0 else length (head m)

    go :: Matrix -> Int -> [Int]
    go mat start
        | start >= nrows || start >= ncols = []
        | otherwise =
            case findMinNonzero mat start of
                Nothing -> []
                Just (pi, pj) ->
                    let mat1 = swapCols start pj (swapRows start pi mat)
                        mat2 = reduce mat1 start
                        d    = (mat2 !! start) !! start
                        d'   = if d < 0 then -d else d
                    in d' : go mat2 (start + 1)

    -- Repeatedly eliminate row and column until stable, then check divisibility.
    reduce :: Matrix -> Int -> Matrix
    reduce mat start =
        let mat1 = elimCol mat start
            mat2 = elimRow mat1 start
            bad  = findNondivisible mat2 start
        in case bad of
            Nothing    -> mat2
            Just (i,_) ->
                -- Adding row i to row start decreases the pivot via GCD.
                let mat3 = addRow mat2 start i
                in reduce mat3 start

    elimCol :: Matrix -> Int -> Matrix
    elimCol mat start = foldr (elimColStep start) mat [start+1 .. nrows-1]

    elimColStep :: Int -> Int -> Matrix -> Matrix
    elimColStep start i mat
        | (mat !! i) !! start == 0 = mat
        | otherwise =
            let pivot = (mat !! start) !! start
                entry = (mat !! i) !! start
                mat'  = if abs entry < abs pivot
                        then swapRows start i mat
                        else mat
                pivot' = (mat' !! start) !! start
                entry' = (mat' !! i) !! start
                q      = entry' `div` pivot'
            in subtractRow mat' i start q

    elimRow :: Matrix -> Int -> Matrix
    elimRow mat start = foldr (elimRowStep start) mat [start+1 .. ncols-1]

    elimRowStep :: Int -> Int -> Matrix -> Matrix
    elimRowStep start j mat
        | (mat !! start) !! j == 0 = mat
        | otherwise =
            let pivot = (mat !! start) !! start
                entry = (mat !! start) !! j
                mat'  = if abs entry < abs pivot
                        then swapCols start j mat
                        else mat
                pivot' = (mat' !! start) !! start
                entry' = (mat' !! start) !! j
                q      = entry' `div` pivot'
            in subtractCol mat' j start q

    findNondivisible :: Matrix -> Int -> Maybe (Int, Int)
    findNondivisible mat start =
        let p = (mat !! start) !! start
        in listToMaybe
               [ (i, j)
               | i <- [start+1 .. nrows-1]
               , j <- [start+1 .. ncols-1]
               , (mat !! i) !! j `mod` p /= 0
               ]

    findMinNonzero :: Matrix -> Int -> Maybe (Int, Int)
    findMinNonzero mat start =
        let candidates = [ (i, j, abs ((mat !! i) !! j))
                         | i <- [start .. nrows-1]
                         , j <- [start .. ncols-1]
                         , (mat !! i) !! j /= 0 ]
        in case candidates of
            [] -> Nothing
            _  -> let (i, j, _) = minimumBy (\(_,_,a) (_,_,b) -> compare a b) candidates
                  in Just (i, j)

    swapRows :: Int -> Int -> Matrix -> Matrix
    swapRows i j mat =
        [ if r == i then mat !! j
          else if r == j then mat !! i
          else mat !! r
        | r <- [0 .. nrows-1] ]

    swapCols :: Int -> Int -> Matrix -> Matrix
    swapCols i j = map swapInRow
      where
        swapInRow row =
            [ if c == i then row !! j
              else if c == j then row !! i
              else row !! c
            | c <- [0 .. ncols-1] ]

    subtractRow :: Matrix -> Int -> Int -> Int -> Matrix
    subtractRow mat target source q =
        [ if r == target
          then zipWith (\a b -> a - q * b) (mat !! r) (mat !! source)
          else mat !! r
        | r <- [0 .. nrows-1] ]

    subtractCol :: Matrix -> Int -> Int -> Int -> Matrix
    subtractCol mat target source q =
        map (\row -> [ if c == target
                       then (row !! c) - q * (row !! source)
                       else row !! c
                     | c <- [0 .. ncols-1] ]) mat

    addRow :: Matrix -> Int -> Int -> Matrix
    addRow mat target source =
        [ if r == target
          then zipWith (+) (mat !! r) (mat !! source)
          else mat !! r
        | r <- [0 .. nrows-1] ]

    listToMaybe [] = Nothing
    listToMaybe (x:_) = Just x

    minimumBy _ [x] = x
    minimumBy f (x:xs) = let m = minimumBy f xs
                         in case f x m of { GT -> m; _ -> x }
    minimumBy _ [] = error "minimumBy: empty list"

-- | Rank of an integer matrix (= number of nonzero invariant factors).
matrixRank :: Matrix -> Int
matrixRank = length . smithFactors
