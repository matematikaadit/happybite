fn main() {
    let mut a = 1;
    let mut b = 1;
    let mut total: int = 0;
    let MAX = 4000000;

    while a < MAX {
        if a%2 == 0 {
            total += a;
        }
        let tmp = a + b;
        a = b;
        b = tmp;
    }
    println(total.to_str());
    // output: 4613732
}
