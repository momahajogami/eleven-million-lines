module Simplicial
    ( Simplex
    , SimplicialComplex
    , fromGenerators
    , simplicesOfDim
    , dimension
    , vertices
    , eulerCharacteristic
    ) where

import Data.List (nub, sort, subsequences)
import Data.Set (Set)
import qualified Data.Set as Set

-- | A simplex is an ordered list of vertex labels (always kept sorted).
type Simplex = [Int]

-- | A simplicial complex: a set of simplices closed under taking faces.
newtype SimplicialComplex = SC { unSC :: Set Simplex }
    deriving (Show)

-- | Build a complex from a list of generators, closing downward under faces.
fromGenerators :: [Simplex] -> SimplicialComplex
fromGenerators gens =
    SC $ Set.fromList $ concatMap (allFaces . sort) gens
  where
    allFaces :: Simplex -> [Simplex]
    allFaces s = filter (not . null) (subsequences s)

-- | All simplices of a given dimension (sorted).
simplicesOfDim :: SimplicialComplex -> Int -> [Simplex]
simplicesOfDim (SC ss) n =
    sort [s | s <- Set.toList ss, length s == n + 1]

-- | Highest dimension of any simplex in the complex.
dimension :: SimplicialComplex -> Int
dimension (SC ss) = maximum (map (\s -> length s - 1) (Set.toList ss))

vertices :: SimplicialComplex -> [Simplex]
vertices k = simplicesOfDim k 0

-- | χ = Σ (-1)^dim (count of simplices of each dim).
eulerCharacteristic :: SimplicialComplex -> Int
eulerCharacteristic (SC ss) =
    sum [(-1) ^ (length s - 1) | s <- Set.toList ss]
