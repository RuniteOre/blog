## Rust & Go in WASM
*My personal experience, documented...*

### Introduction

Recently **Adin** inspired me to take some time learning Rust, mentioning that the WASM builds Rust produces feel particularly useful as they lack a garbage collector and are quite small. After years of using more-or-less just Go for every project I could it didn't seem unreasonable to finally spend some time learning Rust, especially to aid in bringing more fun toys to WASM.

I needed a project to learn with though. I tried using [the Rust book](https://doc.rust-lang.org/book/), along with [the Rust reference](https://doc.rust-lang.org/stable/reference/) however I found the book too slow to dive into the meat of "what's different", and the reference to be too verbose. So I figured I'd think of a project, and use the two as references (I mean, one's even called a reference!). [\*><>](https://esolangs.org/wiki/Starfish) seemed to be the perfect language for such a project as I not only wrote the specification, but I've also created several interpreters in the past, including [a WASM one in Go](https://github.com/redstarcoder/go-starfish/tree/wasm), so I can easily compare the performance/size versus a Rust equivalent.

### Tests & Comparisons

So I did create [a Rust version of the \*><> interpreter](https://github.com/TheDiscordian/rust-starfish), and it was honestly a lot of fun (and of course there was some frustration during some of the learning processes 😉). I also created [a WASM build in Rust](https://github.com/TheDiscordian/rust-starfish-wasm) as well of course. Now, we must compare it to the Go version, as it's very interesting to me to see how different versions of the \*><> interpreter perform against each-other. We can hopefully paint a clear picture of which language has the better \*><> implementation, or at least get some idea of which can achieve the best WASM experience.

#### Size

Size is a big reason why I was so readily open to trying another path for my WASM needs. The **Go version of \*><> with a WASM target is a whopping 2.6MB**, meanwhile the **Rust version is just 168KB**. This makes the **Rust version just 6.5% the size** of the Go version 🤯! As lovely as this is, when I excitedly tweeted about this fact, **Konstantin** inquired about operational performance, so I set out to test that...

#### Performance

The first question I had was "what's the best way to benchmark two different \*><> interpreters?". I figure any answer I come up with won't be considered "fair" so I decided to compare how fast it can do a certain amount of multiplication operations. I ended up settling on 50 million 10×10×10 operations (100 million multiplication ops). The benchmark is done in \*><> itself, I created a script to convert the time since the beginning of the day to seconds, run the 100 million operations, grab the time again, do a simple subtraction, then output the result as a number! This resulting number is how many seconds it took to perform the 100 million operations. What does that script look like?

```
6a*::*h*$m*s++\~6a*::*h*$m*s++$-n;
aaaaaaa*******\a
a*~aa*a*~a-:?!\aa*a*~aa*a*~aa*a*~aa*
```

Above, is my benchmark script. This is the final version anyways, as \*><> allows you to create the same script in many, many ways. This one was modified to try to squeeze as much performance out of the interpreters as possible, if you look closely, the bottom line just repeats the same operation 5 times, `aa*a*~`. This is to eliminate no-ops on the main loop, but I digress...

The **Go implementation in WASM takes 14 seconds to complete** this task on my machine ([try it yourself](https://bafybeieczf46zrbdbp2hgx6lv7hnehri7ocgqt7kf7l42w5sb2jl5qcjpu.ipfs.dweb.link/?script=GwQwVAXBYBZgJAWzAZwNRoDoD9SWnEqhvALQB2A3AFAh33hhPOYi1jZ1jiekQD8AQlbgeXMaI5cgA)), and **the Rust implementation takes just 3-4 seconds** ([try it yourself](https://bafybeiclw34o2cjelgmxwscjzn6y6cozjvxp4e6bdnsp6yi63nrz7vujla.ipfs.dweb.link/?script=GwQwVAXBYBZgJAWzAZwNRoDoD9SWnEqhvALQB2A3AFAh33hhPOYi1jZ1jiekQD8AQlbgeXMaI5cgA)). Rust is the clear winner here, but before you say Go is slow, keep in mind that's just 0.00014ms per operation, so still quite fast. I think it's also important to point out that natively on my M1, the Rust implementation is closer to 57% faster as opposed to the 250% speed increase it enjoys in a WASM environment.

### Conclusions

Rust is awesome! Though I learned I vastly prefer Go's documentation, where I often struggle to figure out what methods are or are not available with Rust's, but maybe time will make that better. A downside to the Rust \*><> WASM interpreter is that sometimes when bad \*><> code is passed, it explodes instead of outputting "something smells fishy...", but there's possibly something I can do to fix that, or maybe future updates will smooth out the WASM experience.

In the end though Rust achieves such a small file size, with the speed it has, and it was relatively the same length line-wise as the Go equivalent. It's definitely going to be my go-to WASM language moving forward.

***Post published: June 3rd, 2022***