# PGP
[Docs](/README.md) > 
[Course Material](/course-material/table-of-contents.md) > [PGP](./table-of-contents.md) > [Chapter One](./chapter-one.md)


# Chapter One
# Instructions to Make gpg Clear-Text Detached Signature

## Create SHA-256 Checksum and Save in File
Take the original file, in this case it's the [Bition white paper in pdf form](https://bitcoin.org/bitcoin.pdf), for signing and create SHA-256 check sum

``` 
shasum -a 256 bitcoin.pdf > bitcoin-manifest.txt
``` 

Check contents with 

```
cat bitcoin-manifest.txt
```

It should look like this.  First part is 256byte checksum in Hex and then filename

```
b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553  bitcoin.pdf
```

## Ceate the gpg Clear-Text Detached Signature of the Checksum File

``` 
gpg --detach-sig --armor bitcoin-manifest.txt
``` 

Check contents with 

```
cat bitcoin-manifest.txt.asc
```

It should look something like this (won't be exact as different each time).

```
-----BEGIN PGP SIGNATURE-----

iQIzBAABCAAdFiEE8077EmOgvmmK4EiJVF/XB8tenWsFAmL2S+EACgkQVF/XB8te
nWujgA/7Bhdj/wosqjSqirsWC48EhKtagET6Z0/fzSI2TpWgfw4JfSzqUX7NYHIs
N2vx5A/zIPpvnHzCe2ysrLRIy4r4CjRIGlCWsdCiIm7K+XRgmyUjD6Sf/hrHRTPu
CS8TrujGgIh6uy/oTxfNomfwhuGppykCFzw8U61z0UeyEZlFOzhzSE3qwXA7dQ6I
AEMXZYE1e6qmYAT7DOLmb5djGsdonvu2xQkv49AGzp6WF890pG+4E8xoO9KGJ3c6
Q8H1NE3YyumzW1N8bfYEGMN67JrphkUS2xA9c3BXnw5pzl3aN9g18b6WsdAgYTiV
Z9OfUxz9tsxPHj5mAv2g4fuhNw7PZjvTeSxIB2kVlcIrjIHNWTHbbYlCOXNDS1ud
CzK8SVxVYJGdkdgKw/cavKfUK/1QTS7piPtOKcuJ1p2hJdtOytFS4nCHkC4UEPX7
LgYYMkBwvc/2UWwggkfm5669hNHylih9zzxsjG1OE7WoPGjFBxSz95KHVjiPnWl+
FuKLYv5pA4ZapuLX5uONUh34r7yqaCogOclS9pqDO7M0ypsqqhUXzYjoy2zsLNoi
077V+zGQChp7x+QMK2fC8AIj2x/ZnedcMzbPoAJbtdxtHXJNHGB39cBk7+COKf2Q
FAXFKmUeWaSodc2vWoIyjv5oqR0MvPCdpf83q4G/ePUGLuFbIgg=
=sjKO
-----END PGP SIGNATURE-----
```

## Verify the Signature

``` 
gpg --verify bitcoin-manifest.txt.asc 
```

Output should be

```
gpg: assuming signed data in 'bitcoin-manifest.txt'
gpg: Signature made Fri 12 Aug 14:47:29 2022 CEST
gpg:                using RSA key F34EFB1263A0BE698AE04889545FD707CB5E9D6B
gpg: Good signature from "CandidateBlock <candidateblock@candidateblock.com>" [ultimate]
```


## What's Next
[Chapter Two](./chapter-two.md)
