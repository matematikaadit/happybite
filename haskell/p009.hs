import Control.Monad (guard)

triplets :: [[Int]]
triplets = do
    c <- [2..1000]
    b <- [1..(c-1)]
    let a = 1000 - b - c
    guard (0 < a && a <= b)
    guard (a*a + b*b == c*c)
    return [a, b, c]

main :: IO ()
main = print . product . head $ triplets
