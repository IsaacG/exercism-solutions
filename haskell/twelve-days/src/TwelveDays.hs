module TwelveDays (recite) where

-- join a list of items together using "," and "and"
-- eg join "dog" "cat" "mouse" => "dog, cat, and mouse"
join :: [String] -> String
join xs =
  foldl (\x y -> x ++ y ++ ", " ) "" (init xs)
  ++ "and " ++ last xs

-- dayItems gives the list of items for a given day.
dayItems :: Int -> String
dayItems n
  | n > 1 = join . reverse . take n $ items
  | otherwise = head items
  where
    items = [
      "a Partridge in a Pear Tree", "two Turtle Doves",
      "three French Hens", "four Calling Birds",
      "five Gold Rings", "six Geese-a-Laying",
      "seven Swans-a-Swimming", "eight Maids-a-Milking",
      "nine Ladies Dancing", "ten Lords-a-Leaping",
      "eleven Pipers Piping", "twelve Drummers Drumming"]

-- recite the verse for a given day.
reciteDay :: Int -> String
reciteDay n =
  "On the "
  ++ (position !! (n - 1))
  ++ " day of Christmas my true love gave to me: "
  ++ dayItems n
  ++ "."
  where
    position = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

recite :: Int -> Int -> [String]
recite start stop = map reciteDay [start .. stop]


-- vim:ts=2:sw=2:expandtab
