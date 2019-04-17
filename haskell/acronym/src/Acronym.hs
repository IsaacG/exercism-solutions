{-# LANGUAGE OverloadedStrings #-}

module Acronym (abbreviate) where

import qualified Data.Char as C
import qualified Data.Text as T
import qualified Data.Tuple as Tuple


isSeparator :: Char -> Bool
isSeparator c
  | c == '-' = True
  | c == '\'' = False
  | C.isSpace c = True
  | C.isLetter c = False
  | otherwise = True

acroStart :: (Char, Char) -> Bool
acroStart (a, b) =
  (C.isLetter a && isSeparator b) ||
  ((C.isUpper a) && not (C.isUpper b))

abbreviate :: String -> String
abbreviate xs =
   T.unpack
   $ T.toUpper
   $ T.cons  -- add in the leading char we stripped
     (T.head $ T.pack xs)
     $ T.pack
       $ map
         Tuple.fst
         $ filter  -- filter using acroStart to compare neighboring letters
           acroStart
           $ T.zip  -- zip input "BarBaz" with "arBaz" to compare neighboring letters
             (maybe "" Tuple.snd $ T.uncons $ T.pack xs)
             (T.pack xs)

-- Much simpler solution ... which fails "HyperText"->"HT"
-- abbreviate xs = T.unpack $ T.toUpper $ T.pack $ map T.head $ T.words $ T.pack xs
