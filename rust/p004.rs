fn reverse(mut num: int) -> int {
    let mut ret = 0;
    while num > 0 {
        ret = ret*10 + num%10;
        num /= 10;
    }
    ret
}

fn palindrome(num: int) -> bool {
    num == reverse(num)
}

fn main() {
    let mut last: int = 0;
    for x in range(900, 1000) {
        for y in range(900, 1000) {
            let n = x * y;
            if n > last && palindrome(n) {
                last = n;
            }
        }
    }
    println(last.to_str())
    // output: 906609
}
