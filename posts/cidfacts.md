## Messing Around With CIDs

This is a short post about converting a CID to raw binary, and back.

### Demonstration

Let's say I have a v0 CID:

```
QmXS8zmXsBVGvdPzj3QFVrzJUcKaaUkEVhHMFvgxUJdVFT
```

I can convert it to a v1 CID:

```shell
$ ipfs cid base32 QmXS8zmXsBVGvdPzj3QFVrzJUcKaaUkEVhHMFvgxUJdVFT
bafybeieheejcn4tspx5re74waw2ixp6hw6rvsssjlf6c3eivcy7oooqjay
```

But that got longer, so what if I wanted to include it in an NFT, using as little data as possible? Well then I'd use the [identity base with raw encoding](https://github.com/multiformats/multicodec/blob/master/table.csv):

```shell
$ ipfs cid format -b identity -c raw bafybeieheejcn4tspx5re74waw2ixp6hw6rvsssjlf6c3eivcy7oooqjay
p ?!&?r}?????Ƿ?YJIY|-?>?:
```

We went from our 46 byte v0 CID, to a 59 byte v1 CID, to a 37 byte raw CID. We can easily go back the same way we initially got the v1 CID as well:

```shell
$ ipfs cid format -b identity -c raw bafybeieheejcn4tspx5re74waw2ixp6hw6rvsssjlf6c3eivcy7oooqjay > rawcid
$ cat rawcid | ipfs cid base32
bafybeieheejcn4tspx5re74waw2ixp6hw6rvsssjlf6c3eivcy7oooqjay
```

### Conclusions

It can be expensive to store data in smart contracts, so hopefully this information helps someone save some bytes. It was just a quick blog post, but in short I'm demonstrating that a CID can be converted to raw binary using [IPLD](https://ipld.io/), and then back. My demonstrations used go-ipfs, but you could do this [in code](http://ipld.io.ipns.localhost:8080/libraries/) as well.

***Post published: June 10th, 2022***