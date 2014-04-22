square   :: Int -> Int
square n = n * n

sumOfSquares   :: Int -> Int
sumOfSquares n = sum $ map square [1..n]

squareOfSum   :: Int -> Int
squareOfSum n = square $ sum [1..n]

diff   :: Int -> Int
diff n = abs $ squareOfSum n - sumOfSquares n

main :: IO ()
main = print $ diff 100
