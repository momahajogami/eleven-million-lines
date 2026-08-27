module Examples
    ( point
    , twoPoints
    , interval
    , circle
    , sphere
    , torus
    , kleinBottle
    , rp2
    , mobiusBand
    ) where

import Simplicial

-- | A single vertex.
point :: SimplicialComplex
point = fromGenerators [[0]]

-- | Two disconnected vertices.
twoPoints :: SimplicialComplex
twoPoints = fromGenerators [[0], [1]]

-- | A single edge — contractible.
interval :: SimplicialComplex
interval = fromGenerators [[0, 1]]

-- | S^1 as the boundary of a triangle.
circle :: SimplicialComplex
circle = fromGenerators [[0,1], [1,2], [0,2]]

-- | S^2 as the boundary of a tetrahedron.
sphere :: SimplicialComplex
sphere = fromGenerators [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]

-- | T^2 via the standard 9-vertex triangulation.
--   v i j = 3*(i mod 3) + (j mod 3). Opposite sides identified.
torus :: SimplicialComplex
torus = fromGenerators
    [ [v i j, v i (j+1), v (i+1) (j+1)]
    | i <- [0..2], j <- [0..2]
    ] ++
    fromGenerators
    [ [v i j, v (i+1) j, v (i+1) (j+1)]
    | i <- [0..2], j <- [0..2]
    ]
  where
    v i j = 3 * (i `mod` 3) + (j `mod` 3)
    fromGenerators gs1 `mappend` fromGenerators gs2 =
        fromGenerators (gs1 ++ gs2)

-- Haskell doesn't know about our fromGenerators returning SimplicialComplex
-- without a Semigroup instance, so let's be explicit:
torus = fromGenerators $
    [ [v i j, v i (j+1), v (i+1) (j+1)] | i <- [0..2], j <- [0..2] ] ++
    [ [v i j, v (i+1) j, v (i+1) (j+1)] | i <- [0..2], j <- [0..2] ]
  where v i j = 3 * (i `mod` 3) + (j `mod` 3)

-- | Klein bottle — horizontal identification with flip.
--   v(i, 3) = v(2-i, 0) instead of v(i, 0).
kleinBottle :: SimplicialComplex
kleinBottle = fromGenerators $
    [ [v i j, v i (j+1), v (i+1) (j+1)] | i <- [0..2], j <- [0..2] ] ++
    [ [v i j, v (i+1) j, v (i+1) (j+1)] | i <- [0..2], j <- [0..2] ]
  where
    v i j
        | j `mod` 3 == 0 && j > 0 = 3 * ((2 - i `mod` 3) `mod` 3) + 0
        | otherwise                 = 3 * (i `mod` 3) + (j `mod` 3)

-- | RP^2 — minimal triangulation with 6 vertices, 15 edges, 10 triangles.
rp2 :: SimplicialComplex
rp2 = fromGenerators
    [ [0,1,2], [1,2,3], [2,3,4], [3,4,0], [4,0,1]
    , [0,2,5], [2,4,5], [4,1,5], [1,3,5], [3,0,5]
    ]

-- | Möbius band — deformation retracts to a circle. H_1 = ℤ.
mobiusBand :: SimplicialComplex
mobiusBand = fromGenerators
    [ [0,1,5], [1,5,6]
    , [1,2,6], [2,6,7]
    , [2,3,7], [3,7,8]
    , [3,4,8], [4,8,9]
    , [4,0,9], [0,9,5]
    ]
