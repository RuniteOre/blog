## How to steal this blog

Heya! You like my blog? Want your own? Well, you've come to the right place. This is the first post in what'll possibly be a series of posts on how to setup your own esoteric blog. Hit me up wherever you can find me if you have any questions.

### How to contact me

- Discord: Discordian#3926
- [Filecoin Slack](https://filecoin.io/slack): Discordian
- Twitter: @TRDiscordian

Seems like enough contact information ... unfortunately there's no [web3](https://chat.thedisco.zone) way to ping me right now.

### Requirements

So I want to keep this post focused on the topic of how to easily clone IPFS websites. If you're totally brand new to IPFS you might need to do some setup to *completely* follow along, but it shouldn't be so bad. After all, once it's all setup and configured once, that's it, right?

- [go-ipfs CLI](https://docs.ipfs.io/install/command-line/): We'll be using `ipfs` commands in this tutorial, so having access to the go-ipfs CLI (with the daemon running!) will be critical here.
- Text editor

...I intended to have a whole list of requirements here, but that's honestly it. Having your NAT open or port 4001 forwarded will also go a long way here, though in theory go-ipfs should punch the NAT.

#### Optional

- Some HTML/CSS skills will help
- Port 4001 forwarded (TCP/UDP)
- [Fleek](https://fleek.co): Very useful if you want a service to handle the IPNS stuff for you, it will make data available over IPFS, backed up to Filecoin
- [web3.storage](https://web3.storage): What's not to love about it? Free 1TiB space available over IPFS, backed up to Filecoin

You probably don't need both Fleek and web3.storage, but if you haven't heard of either of them, both are worth your time to check out. Fleek could reduce your manual work, both Fleek and web3.storage will make your blog more "available" (it won't be just your PC hosting the content).

### Stealing the blog

1. Ensure your IPFS daemon is running (at minimum, you'll want to start it somewhere with `ipfs daemon`).
2. Open a terminal in the directory of your choosing and run `ipfs get /ipns/blag.thedisco.zone`
3. Notice the blog has now been downloaded into a directory named `blag.thedisco.zone` (you can view it in your favourite file explorer!)

Now you have it! Wasn't that easy? ... but you probably want to personalise it. That's (IMHO) also pretty easy, but the difficulty / time will vary depending on what you want to do. For this entry, we'll just focus on adding posts, and updating an IPNS key. Maybe I can do future posts on other features if there's interest in that, or I just feel like making a tutorial about it :).

Note: *You might notice the blog doesn't function out of the box, simply add the entire blog, and load up the resulting CID in your favourite browser via:* `ipfs add -r <directory of blog>`

### Adding a post

This blog simply uses markdown to parse the posts, then renders them in HTML ([check out the posts directory](./posts)). So all you need to do is first, make your markdown file, then after, update `index.html`. Specifically, you want to scroll down to the "main-nav" element, and add an entry. Let's say you placed your post in the posts directory named "firstpost.md", with the title "My First Blog Post", and this was your only post, you'd update the list to look liks this:

```html
<ul id="main-nav" class="main-nav" style="top:calc(-1em - 4px);height:calc(100% + 1em - 8px);">
	<li onclick="loadContent(this, 'firstpost')"><a href="javascript:void(0)">My First Blog Post</a></li>
</ul>
```

Effectively each entry ("entry" referring to the line beginning with `<li` in the above example) just needs to know what the name of the markdown file is (without extension) and the title (so the user knows what the post is called!):

```html
<li onclick="loadContent(this, 'FILENAME_WO_EXTENSION')"><a href="javascript:void(0)">VERY LOUD TITLE</a></li>
```

### Updating / obtaining the IPNS key

So sharing the CID of your blog is fine, but every time you add or update a post, you get a new CID! We resolve this with [IPNS](https://docs.ipfs.io/concepts/ipns/). First we must create our IPNS key (and name it!), then we take our CID each time we update it, and re-publish it via the go-ipfs daemon using IPNS. Fleek can do this for you automatically, but I'm sticking to explaining how to do it manually here.

#### Creating the key

Creating the key is simple:

```shell
ipfs key gen blag
```

Where "blag" is the name of your key. This only ever has to be done once, this generates a keypair on your node with the name "blag", the resulting public key is what you'll ultimately share for others to reach your blog.

#### Updating the blog

You can simply update the blog with:

```shell
ipfs add -rQ <path_to_blog_directory> | ipfs name publish -k <name_of_key>
```

The `ipfs add` gets us the CID of the directory (and makes it available through your node), and `ipfs name publish` will update our IPNS key for us :). The resulting output should be something like this:

```
Published to k51qzi5uqu5di6xzhryqhi9wknd53mbn0sx1cjehwtc2kggpfl5bssuomk3i5f: /ipfs/QmNdkZHHK9UgBy7w1djsQk3aDj78MYjh7AKa5zStoGmBkn
```

So you could access your blog by going to a URL like "[https://k51qzi5uqu5di6xzhryqhi9wknd53mbn0sx1cjehwtc2kggpfl5bssuomk3i5f.ipns.dweb.link/](https://k51qzi5uqu5di6xzhryqhi9wknd53mbn0sx1cjehwtc2kggpfl5bssuomk3i5f.ipns.dweb.link/)".

### Conclusions

I hope you learned something from this post, or at least find it useful in some way. If you want a pretty URL (like blag.thedisco.zone) then I highly recommend you read up on [DNSLink](https://docs.ipfs.io/concepts/dnslink/) which is insanely useful. My contact info is at the top of this post, feel free to hit me up if you want a post about any of the topics you feel like I might have glossed over, something you'd like a tutorial on, or whatever. I'm pretty open to putting all sorts of content on this blog.


***Post published: May 4th, 2022***