module Clock (addDelta, fromHourMin, toString) where

import Text.Printf

data Clock = Clock Int Int
  deriving (Eq)

fromHourMin :: Int -> Int -> Clock
fromHourMin hour mn = Clock
  (mod (hour + (div mn 60)) 24)
  (mod mn 60)

toString :: Clock -> String
toString (Clock hr mn) = printf "%02d:%02d" hr mn

addDelta :: Int -> Int -> Clock -> Clock
addDelta deltaH deltaM (Clock hr mn) =
  Clock
    (
      mod
        ( deltaH + ( hr + ( div (deltaM + mn) 60 ) ) )
      24
    )
    $ mod (deltaM + mn) 60
