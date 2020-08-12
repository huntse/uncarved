+++
title = "Writing an Automated Marketmaking System"
description = "The first in a series of articles in which we will construct a simple high frequency trading system."
aliases = [ "/articles/mm_1" ]
date = 2011-05-11T09:59:07Z
[taxonomies]
tags = ["computers"]
+++


There has been a lot of press recently about the evils of high
frequency trading (HFT), with many commentators saying that HFT may
well be the root of the next big financial crisis. The basis for this
view is the increasing importance of computerised market-making systems
in providing liquidity to markets, and the concern about what happens
if these participants stop providing this liquidity in the event of
some sort of market panic. Additionally, some commentators maintain
that automated market makers are trading in a manner that is to the
detriment of other participants.

Rather than attempting to add more commentary to this debate, I'd like
to contribute in a practical way by widening the understanding of these
systems so that people can decide for themselves. As such, this is
going to be the first in a series of articles during which we will
build a fully-functional electronic market-making system. It's going to
take a little while to develop all the pieces, but since I have the
first piece almost ready to go I think it's time I came out with the
introductory articles. This series will mostly be aimed at people with
some computing background and interest in financial markets but not
assume any knowledge of how markets work.

Caveats before we begin

Nothing in these articles is going to constitute any sort of advice as
to the merits of investing in a particular product, or making markets
using a particular strategy. If you follow the series you will acquire
some bits of software which can be used to construct an EMM (Electronic
Market-Making) system. I won't make you pay for them, and if you use
them, you may lose money. The software may have bugs or unintended
features which cause you to lose money. I'm really sorry if that's the
case. You need to understand the software and accept the consequences
of what it does, because it will be trading on your account. You need
to put in place any tests you require to feel happy that it is
performing according to your specifications. You also need to
understand that in financial markets you are dealing with random
processes and as such even well-founded strategies can lead to losses.
Additionally, anything you make using this toolkit will need to be able
to hold it's own against other market participants who will be aiming
to exploit it. In any financial situation you need to do your own
research and take responsibility for what happens - this is no
different. Obviously you shouldn't put more at risk than you can afford
to lose, but it's your money, and you need to decide whether this is
right for you.

Background - Marketmakers and liquidity

It would be very cumbersome if every time you wanted to buy something
you had to find the person willing to sell exactly that quantity at
that time and agree a price, so generally when we buy or sell, a
[marketmaker][5] actually takes the other side of the trade, hoping to
find someone else wanting the opposite bargain later in the day. The
marketmaker makes money by charging a small spread (ie they buy for
lower than they sell for) in return for assuming the risk of holding
the position you have put them into until they are able to unwind it by
doing the opposite trade. This risk is a function of the ease of the
unwind (how likely they are to be able to find someone to trade with)
and the [price][6] volatility of the asset. So if you want to trade in a
product which has very low price volatility, and very high
[liquidity,][7] then it would be easy for the marketmaker to find someone
to trade out of their position with, and they would not need to worry
about the price moving too much while they hold the asset, so you would
expect the spread between the bid and ask prices to be very low.
Conversely, high volatility and low liquidity assets would normally
have high spreads to compensate marketmakers for their higher risk.

Providing liquidity

In the old days, the position of marketmaker was held only by exchange
locals who had to pay for the membership that allowed them to earn this
spread, but with the advent of [limit][8] order books, anyone can provide
liquidity to many markets and expect to be compensated for it. Our goal
is to write a computer system which will do this for us. In order to do
that, we first need to understand how a limit order book works, and by
way of an example I'm going to jump right in and introduce the market
we will use as the basis for this whole series.

Bullionvault

The market we're going to use for our examples is [bullionvault.com,][9]
which is in essence a physical gold and silver market, with all the
actual metal held in escrow in reserves in New York, London and Zurich,
with seperate order books in $, £ and €. If you sign up using that link
I will make a small referral fee (at no cost to you) from the
commissions you pay to trade your account, and that's I'm going to get
for writing these articles. Before you sign up, you should of course,
peruse the [on-line][10] help so you understand how their system works,
and like any other investment, you should think carefully about the
risks involved.

Understanding the order book

If you go to the [front][11] page, you can see the current sell and buy
prices for gold in the three locations in one currency (USD by
default).

Bullionvault USD gold touch prices

The touch

These prices are just the top of the order book - the so-called touch
prices. You would find more quantity available at different prices to
buy or sell further away in the book, but what the prices mean in this
example is that if you wanted to buy one troy ounce of gold in NYC it
would cost you $1528, but if you wanted to sell you would only get
$1524, so the market spread is $4 per TOz or $110 per kg if you live in
the modern world. We're going to use metric units for these articles as
teaching something as amazing as a modern computer to think in Troy
ounces (or any imperial units) is a great evil, like teaching children
arithmetic only by using Roman numerals or something.

Bid and Offer

We're also going to use some real market-making terminology, so we're
going to refer to bid and ask or bid and offer prices, rather than sell
and buy prices. The easy way to remember which way round these are is
to think about the fact that as marketmakers we want to make money and
so charge people for what they want to do. If they want to sell, we're
going to bid to buy those shares from them at a low price. If they want
to sell, we will reluctantly offer to sell to them at a high price.
Hence bid is low and offer is high. When these prices are reversed, the
orderbook is said to be crossed. This happens in equity markets when
they are closed for the night, there is then an auction phase where
high bids are matched with low offers until the book is uncrossed and
normal trading begins. We wouldn't expect the orderbook to be crossed
in a continuous trading market like this unless something was wrong and
matching was suspended.

Aggressive and Passive

If an order to buy comes in, and it has no limit price, it is matched
with the cheapest available sell orders until it is filled. If it has a
limit price, it will only be filled up to the limit price on the order.
But what happens to the remaining quantity? Under normal circumstances,
this quantity stays on the book at the limit price until it can be
matched against an incoming sell order within its limit.

We say that an order that provides liquidity by sitting on the book
waiting to be filled is passive and that an order which crosses the
spread, taking liquidity from the market by crossing off with passive
orders is aggressive. We can also refer to the passive touch and
aggressive touch. If we have an order to buy, then the passive touch is
the bid and the aggressive touch is the offer. This is because if we
want to buy passively, we will place our order at the bid or lower,
whereas if we want to buy aggressively, we will need to pay the offer
or higher. The opposite would be true for a sell order. If we want to
sell right now, we will need our limit price to be at, or more
aggressive (lower) than, the current bid, whereas if we are prepared to
wait, our price can be more passive (ie higher).

Still to come - the software

In the next article, I will introduce a the software we can use to
connect to bullionvault. Please feel free to comment below if anything
so far is unclear and I'll try to deal with it in the next article.

[1]: http://www.uncarved.com/articles/mm_1
[2]: http://www.uncarved.com/
[3]: http://www.uncarved.com/articles/contact
[4]: http://www.uncarved.com/login/
[5]: http://www.investopedia.com/terms/m/marketmaker.asp
[6]: http://www.investopedia.com/terms/v/volatility.asp
[7]: http://www.investopedia.com/terms/l/liquidity.asp
[8]: http://www.investopedia.com/terms/l/limitorderbook.asp
[9]: http://www.bullionvault.com/#HUNTSE
[10]: http://www.bullionvault.com/help/index.do
[11]: http://www.bullionvault.com/#HUNTSE
[12]: http://www.uncarved.com/tags/computers
