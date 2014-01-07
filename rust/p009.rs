fn main() {
    for a in range(1, 500) {
        let low = std::num::max(a, 500-a);
        for b in range(low, 500) {
            let c = 1000 - a - b;
            if a*a+b*b == c*c {
                println!("{}", a * b * c)
                // output: 31875000
            }
        }
    }
}
