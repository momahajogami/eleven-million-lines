module Boundary
    ( boundaryMatrix
    , verifyBoundarySquaredZero
    ) where

import Data.List (elemIndex, sort)
import Data.Maybe (mapMaybe, fromMaybe)
import Simplicial

-- | Integer matrix as a list of rows.
type Matrix = [[Int]]

-- | Compute the boundary matrix ∂_n for the given complex.
--
--   Result is an (m × k) integer matrix where:
--     m = number of (n-1)-simplices  (rows)
--     k = number of n-simplices      (cols)
--
--   Entry (i,j) = coefficient of the i-th (n-1)-simplex
--                 in the boundary of the j-th n-simplex.
--
--   Returns an empty matrix for n = 0 or when no n-simplices exist.
boundaryMatrix :: SimplicialComplex -> Int -> Matrix
boundaryMatrix k 0 = []
boundaryMatrix k n =
    let nSimps   = simplicesOfDim k n
        nm1Simps = simplicesOfDim k (n - 1)
    in if null nSimps || null nm1Simps
       then []
       else [ [ coeff tau sigma | sigma <- nSimps ]
            | tau <- nm1Simps ]
  where
    nm1Simps = simplicesOfDim k (n - 1)

    coeff :: Simplex -> Simplex -> Int
    coeff tau sigma =
        case faceSign tau sigma of
            Just s  -> s
            Nothing -> 0

    -- | If tau is a face of sigma, return the sign (-1)^l where l is
    --   the index of the omitted vertex. Otherwise Nothing.
    faceSign :: Simplex -> Simplex -> Maybe Int
    faceSign tau sigma
        | length tau /= length sigma - 1 = Nothing
        | otherwise =
            case [ l | l <- [0 .. length sigma - 1]
                     , dropAt l sigma == tau ] of
                [l] -> Just ((-1) ^ l)
                _   -> Nothing

    dropAt :: Int -> [a] -> [a]
    dropAt i xs = take i xs ++ drop (i + 1) xs

-- | Verify ∂_{n-1} ∘ ∂_n = 0 for all n. Should always be True.
verifyBoundarySquaredZero :: SimplicialComplex -> Bool
verifyBoundarySquaredZero k =
    all check [1 .. dimension k]
  where
    check n =
        let dn   = boundaryMatrix k n
            dnm1 = boundaryMatrix k (n - 1)
        in null dn || null dnm1 || isZeroMatrix (matMul dnm1 dn)

    isZeroMatrix m = all (all (== 0)) m

    matMul :: Matrix -> Matrix -> Matrix
    matMul a b
        | null a || null b || null (head b) = []
        | otherwise =
            [ [ sum (zipWith (*) rowA colB) | colB <- transpose b ]
            | rowA <- a ]
      where
        transpose [] = []
        transpose ([] : _) = []
        transpose xss = map head xss : transpose (map tail xss)
