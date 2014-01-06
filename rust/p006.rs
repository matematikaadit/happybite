fn main() {
    let mut a = 0;
    let mut b = 0;
    for i in range(1,101) {
        a += i;
        b += i * i;
    }
    println(fmt!("%?",a*a - b));
    // output: 25164150
}
