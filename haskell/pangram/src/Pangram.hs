module Pangram (isPangram) where

import qualified Data.Char as C

-- Any a in [a]
iany :: Ord a => a -> [a] -> Bool
iany c (x:xs)
  | x == c = True
  | otherwise = iany c xs
iany _ [] = False

-- All a in [a]
iall :: Ord a => a -> [a] -> Bool
iall c (x:xs)
  | x /= c = False
  | otherwise = iall c xs
iall _ [] = True

isPangram :: String -> Bool
isPangram text = iall True $ map (\ x -> iany x ctext ) lower
  where
    -- Lowercase and extract letters
    ctext = map C.toLower $ filter C.isLetter text
    lower = ['a','b'..'z']

-- vim:ts=2:sw=2:expandtab
