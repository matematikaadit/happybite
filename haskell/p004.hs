palindrome :: Int -> Bool
palindrome n = reverseNum n == n

reverseNum :: Int -> Int
reverseNum = read . reverse . show

largestPalProd :: Int -> Int -> Int
largestPalProd up down = f up up 0
    where
      f                     :: Int -> Int -> Int -> Int
      f a b n
        | a < down          = n
        | b < a || a*b <= n = f (a-1) up n
        | palindrome (a*b)  = f a (b-1) (a*b)
        | otherwise         = f a (b-1) n

main :: IO ()
main = print $ largestPalProd 999 100
