palindrome :: Int -> Bool
palindrome n = reverseNum n == n

reverseNum :: Int -> Int
reverseNum = read . reverse . show

largestPalProd :: Int -> Int -> Int
largestPalProd top down = f top top minBound
    where
      f                     :: Int -> Int -> Int -> Int
      f a b n
        | a < down        = n
        | b < a || c <= n = f (a-1) top n
        | palindrome c    = f a (b-1) c
        | otherwise       = f a (b-1) n
        where c = a * b

main :: IO ()
main = print $ largestPalProd 999 100
