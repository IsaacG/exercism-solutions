module BST
    ( BST
    , bstLeft
    , bstRight
    , bstValue
    , empty
    , fromList
    , insert
    , singleton
    , toList
    ) where

-- Trees are made of nodes which each got a value and a right/left tree.
-- Use a record to get bstValue/bstLeft/bstRight for free.
data BST a = BST {
  bstValue :: Maybe a,
  bstLeft  :: Maybe (BST a),
  bstRight :: Maybe (BST a)
} deriving (Eq, Show)

empty :: BST a
empty = BST Nothing Nothing Nothing

-- foldl -> start with an empty tree -> reduce: insert elements
fromList :: Ord a => [a] -> BST a
fromList xs = foldl (\t v -> insert v t) empty xs

-- Insert an element into a (Maybe BST), always returning a (Just BST)
maybeNew :: Ord a => a -> Maybe (BST a) -> Maybe (BST a)
maybeNew x Nothing = Just ( BST (Just x) Nothing Nothing )
maybeNew x (Just y) = Just ( insert x y )

insert :: Ord a => a -> BST a -> BST a
insert x (BST Nothing l r)  = BST (Just x) l r
insert x (BST (Just v) l r)
  | x <= v = BST (Just v) (maybeNew x l) r
  | otherwise = BST (Just v) l (maybeNew x r)

-- Tree with one element. Insert element into empty tree.
singleton :: Ord a => a -> BST a
singleton x = insert x empty

maybeToList :: Maybe(BST a) -> [a]
maybeToList Nothing = []
maybeToList (Just (BST Nothing _ _)) = []
maybeToList (Just (BST (Just x) l r)) = (maybeToList l) ++ [x] ++ (maybeToList r)

toList :: BST a -> [a]
toList x = maybeToList (Just x)

-- vim:expandtab:ts=2:sw=2
