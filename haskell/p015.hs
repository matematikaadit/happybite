latice :: [[Integer]]
latice = iterate (scanl1 (+)) (repeat 1)

main :: IO ()
main = print $ latice !! 20 !! 20
