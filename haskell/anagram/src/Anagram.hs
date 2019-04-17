{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE OverloadedStrings #-}

module Anagram (anagramsFor) where
import Data.Text as T

anagramsFor :: String -> [String] -> [String]
anagramsFor xs xss = Prelude.filter (\x -> isMatchS x xs) xss

isMatchS :: String -> String -> Bool
isMatchS x y
  -- Words are apparently not anagrams of themselves
  | (T.toLower $ T.pack x) == (T.toLower $ T.pack y) = False
  -- Lose case, make Text and check
  | otherwise = isMatch (T.toLower $ T.pack x) (T.toLower $ T.pack y)

isMatch :: Text -> Text -> Bool
isMatch x y
  | x == y = True
  -- Check length for differences.
  | not ((T.length x) == (T.length y)) = False
  -- Check if the first char of x is missing from y.
  | T.findIndex (\z -> z == (T.head x)) y == Nothing = False
  | otherwise =
    isMatch
      (T.filter (\z -> z == (T.head x)) x)
      (T.filter (\z -> z == (T.head x)) y)
    

