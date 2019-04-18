module Luhn (isValid) where

import Data.Char
import Data.Text as T

-- Drop non-digits
clean :: Text -> Text
clean a = T.filter (\x -> isDigit x) a

-- Get even-length strings
pad :: Text -> Text
pad n
  | mod (T.length n) 2 == 0 = n
  | otherwise = cons '0' n

-- Extract a Char and convert to Int
toInt :: (Text -> Char) -> Text -> Int
toInt p s = read [(p s)] :: Int

-- Multiply by 2. If the result is 10 or more, subtract 9.
doubleish :: Int -> Int
doubleish n
  | n < 5 = 2 * n
  | otherwise = (2 * n) - 9

-- Double(ish) the leading digit and add the latter.
partValue :: Text -> Int
partValue p = (+)
              (toInt T.last p)
              $ doubleish $ toInt T.head p

-- Clean and split the string into chunks and sum up each part.
sumValue :: String -> Int
sumValue s =
  let parts = chunksOf 2 . pad . clean . pack $ s
  in sum $ Prelude.map partValue parts

isValid :: String -> Bool
isValid n
  | (T.length . clean . pack $ n) <= 1 = False
  | otherwise = (==) 0 $ mod (sumValue n) 10

