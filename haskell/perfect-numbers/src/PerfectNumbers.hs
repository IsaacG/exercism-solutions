module PerfectNumbers (classify, Classification(..)) where

data Classification = Deficient | Perfect | Abundant deriving (Eq, Show)

isDiv :: Int -> Int -> Bool
isDiv x y = (mod x y) == 0

factors :: Int -> [Int]
factors n = filter (isDiv n) [1,2..(n-1)]

classify :: Int -> Maybe Classification
classify n
  | n < 1 = Nothing
  | s == n = Just Perfect
  | s < n = Just Deficient
  | s > n = Just Abundant
  | otherwise = error "Not possible!"
  where s = sum . factors $ n
