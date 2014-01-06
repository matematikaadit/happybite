fn lcd(a: i64, b: i64) -> i64 {
    a * b / gcd(a, b)
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a%b)
    }
}

fn main() {
    let mut result: i64 = 1;
    let mut i: i64 = 1;
    while i <= 20 {
        result = lcd(result, i);
        i += 1;
    }
    println(result.to_str());
    // output: 232792560
}
