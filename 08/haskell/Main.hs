module Main where

import Simplicial
import Homology
import Examples

main :: IO ()
main = do
    describe "Point"                    point
    describe "Two disjoint points"      twoPoints
    describe "Interval [0,1]"           interval
    describe "Circle S^1"               circle
    describe "Sphere S^2"               sphere
    describe "Torus T^2"                torus
    describe "Klein bottle"             kleinBottle
    describe "Real projective plane RP^2" rp2
    describe "Möbius band"              mobiusBand

    putStrLn "Euler characteristic consistency checks:"
    mapM_ checkEuler
        [ ("circle",       circle)
        , ("sphere",       sphere)
        , ("torus",        torus)
        , ("kleinBottle",  kleinBottle)
        , ("rp2",          rp2)
        ]
  where
    checkEuler (name, k) =
        let chi1 = eulerCharacteristic k
            chi2 = eulerFromBetti k
            ok   = chi1 == chi2
        in putStrLn $ (if ok then "  ✓ " else "  ✗ ") ++ name
                    ++ ": χ_simplicial=" ++ show chi1
                    ++ ", χ_Betti=" ++ show chi2
