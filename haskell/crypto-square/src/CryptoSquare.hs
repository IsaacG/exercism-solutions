module CryptoSquare (encode) where

import Data.Char
import Data.Text as T

-- Helper to test Text things out
withText :: (Text -> Text) -> String -> String
withText p s = T.unpack . p . T.pack $ s

-- Strip out non-alpha
clean :: Text -> Text
clean t = T.filter isAlphaNum $ T.toLower t

-- Roughly we want ceil(sqrt), floor(sqrt)
est :: Int -> (Int, Int)
est x =
  let
    sq = sqrt $ fromIntegral x :: Float
  in (ceiling sq, floor sq)

tupleMult :: (Int, Int) -> Int
tupleMult (a, b) = a * b

-- Add one to the X if it's not big enough as the ceil/floor thing doesn't quite work.
dimensions :: Int -> (Int, Int)
dimensions x =
  (
    (fst . est $ x),
    (+)
      (snd . est $ x)
      -- Add 1 if we need more space. Otherwise 0.
      (if (tupleMult . est $ x) < x then 1 else 0)
  )

-- Space-pad the text so it fills the box
pad :: Text -> Text
pad t =
  let needed = tupleMult . dimensions . T.length $ t
  in T.justifyLeft needed ' ' t

-- Chunk up the text into x chunks of y
chunks :: Text -> [Text]
chunks t =
  let y = fst . dimensions . T.length $ t
  in T.chunksOf y t

-- Group the Nth char from each string.
rotate :: [Text] -> [Text]
rotate t
  | (==) 0 $ Prelude.length t = []
  | (==) 0 $ T.length . Prelude.head $ t = []
  | otherwise =
      (:)
        (pack $ Prelude.map T.head t)
        (rotate $ Prelude.map T.tail t)
  
encode :: String -> String
encode xs = withText ( T.unwords . rotate . chunks . pad . clean ) xs
