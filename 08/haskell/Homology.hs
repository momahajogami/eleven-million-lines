module Homology
    ( HomologyGroup(..)
    , homology
    , allHomology
    , eulerFromBetti
    , describe
    ) where

import Simplicial
import Boundary
import Smith

data HomologyGroup = HomologyGroup
    { hDim    :: Int
    , hBetti  :: Int      -- rank of free part
    , hTorsion :: [Int]   -- torsion coefficients > 1
    } deriving (Eq)

-- | H_n = ℤ^β ⊕ ℤ/d_1ℤ ⊕ ... ⊕ ℤ/d_kℤ
instance Show HomologyGroup where
    show (HomologyGroup n b ts) =
        "H_" ++ show n ++ " = " ++ showGroup b ts

showGroup :: Int -> [Int] -> String
showGroup 0 []  = "0"
showGroup b ts  = intercalate " ⊕ " parts
  where
    parts = freePart ++ map torsionPart ts
    freePart
        | b == 0    = []
        | b == 1    = ["ℤ"]
        | otherwise = ["ℤ^" ++ show b]
    torsionPart d = "ℤ/" ++ show d ++ "ℤ"

    intercalate _ []     = ""
    intercalate _ [x]    = x
    intercalate sep (x:xs) = x ++ sep ++ intercalate sep xs

-- | Compute H_n of a simplicial complex.
homology :: SimplicialComplex -> Int -> HomologyGroup
homology k n =
    let kn    = length (simplicesOfDim k n)
        dn    = boundaryMatrix k n
        rn    = matrixRank dn
        dnp1  = boundaryMatrix k (n + 1)
        (rnp1, torsion) =
            if null dnp1
            then (0, [])
            else let fs = smithFactors dnp1
                 in (length fs, filter (> 1) fs)
        betti = kn - rn - rnp1
    in HomologyGroup n betti torsion

-- | Compute H_n for n = 0, 1, ..., dim(K).
allHomology :: SimplicialComplex -> [HomologyGroup]
allHomology k = map (homology k) [0 .. dimension k]

-- | χ = Σ (-1)^n β_n.
eulerFromBetti :: SimplicialComplex -> Int
eulerFromBetti k =
    sum [(-1)^n * hBetti g | (n, g) <- zip [0..] (allHomology k)]

-- | Print a readable homology summary.
describe :: String -> SimplicialComplex -> IO ()
describe name k = do
    putStrLn $ replicate 50 '─'
    putStrLn $ "  " ++ name
    putStrLn $ replicate 50 '─'
    putStrLn $ "  dim = " ++ show (dimension k)
             ++ ", χ = " ++ show (eulerCharacteristic k)
    mapM_ printGroup (allHomology k)
    putStrLn ""
  where
    printGroup g@(HomologyGroup _ b ts)
        | b == 0 && null ts = putStrLn $ "     " ++ show g
        | otherwise          = putStrLn $ "  →  " ++ show g
