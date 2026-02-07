---
layout: post
mathjax: false
comments: true
title:  "Go as a Prototypical Strategy Game"
date:   2023-05-18 05:45:53 +0000
categories: gamedev
---

<!-- A63 -->

Go and chess are two classic strategy games with simple rules that are
hard to master.
Go arguably has simpler rules than chess, but the game is arguably
the harder of the two to master.
Go is essentially what you get if a strategy is reduced to the minimum
number of possible components.
Go gets a lot of things right.
This post will discuss the scope of Go's rules, and discuss why it is an
important study for modern game design.

## Go Game Scope

This section will cover the scope of Go without going into details.
Readers are expected to know the rules, or know how to find them.
A typical go set includes the following.

* one 19x19 board
* 181 black stones
* 180 white stones

Different sized Go boards are played on, and a non-standard  board
is typically going to be square with the length of the sides being an odd
number.
Note that 19x19 is 361.
This implies that a set has enough stones to fill the whole board,
with black getting the extra odd stone because it moves first.
The following board sizes are also used.

* 9x9 for very short games to teach beginners
* 13x13 for short games to teach beginners
* 17x17 is the historical board size

Note that Go only has one kind of game token- stones.
Black and white stones are mechanically identical and differ only in who
controls them.
Go is a battle for territorial control, and stones could abstractly be
considered soldiers on a battlefield.

Players take turns placing stones, starting with black.
If black receives a handicap, the handicap stones are placed and then white
moves (black is the weaker player).
Groups of stones that are completely surrounded are removed from the board.
Passing is legal, but it is only beneficial at the end of the game.

The basic concepts of Go include the following.

* liberties - the number of open spaces adjacent to a group of stones
* eyes - the number of open areas inside a group of stones
* live string - any group with two or more eyes cannot be captured
* dead string - isolated groups that cannot form two eyes

Go has a few additional rules.

* ko - reverting the game state to the one on your previous turn is not allowed to prevent endless loops
* seki - a local stalemate where opposing groups do not have two eyes, but they cannot capture each other either

All else being equal, Go is a game where a player who understands the game
better will consistently beat weaker opponents.
Go has a handicap system where the game starts off unequally, and this
allows players of different skill levels to enjoy playing against one
another.
The difference in player grade levels indicates the number of hanicap
stones, and the weaker player starts with anywhere from two to nine
extra stones.

Black has an advantage because it moves first.
If players are of equal skill, white starts with bonus points called komi.
Over millennia of play, people have determined that playing first is worth
about sevent points.
Tournaments typically give white seven and a half points to eliminate
the possibility of a draw.

## Game Complexity Implications

The complete game state for a game of Go can be represented in under one
hundred bytes if it is optimized for size.

* 361 bits (46 bytes) for white stone locations
* 361 bits (46 bytes) for black stone locations
* 1 or 2 bytes for captured black stones (and 7-point komi)
* 1 or 2 bytes for captured white stones
* 0 bits komi (white implicity get an extra half point)
* 1 bit to indicate the active player
* 1 bit to indicate if the game is over
* 1 bit to indicate if the current player conceded
* 1 bit to indicate if the previous player passed
* 10 bits (2 bytes) for the coordinates of the previous black move (ko)
* 10 bits (2 bytes) for the coordinates of the previous white move (ko)

46 bytes contains 368 bits.
92 bytes for all stone locations works out to 14 unused bits.
Four of these can be used for game state flags.
Captured stones can then be stored in one byte and any remaining bits.
Add four more bytes to store information for determining ko, and the
total state is 98 bytes.

Alternatively, one byte can be used for each board location and flag, four
bytes can be used for each player's score for a total of 373 bytes.
Add another 16 bytes for ko and the grand total is 389 bytes, or about 400.

The complexity of Go is not in the static game state, but in the possible
number of game states.
Each board location can have a black stone, a white stone, or it can be
empty.
This works out to 3 to the power of 361 possible board states,
or a number so large it is a one followed by 172 zeros.
Despite many of those states being illegal, the magnitude of possibilities
is way over one googol.
This is far too many for static analysis without accounting for captured
stones, passing, or ko.

For comparison, a chess board has 64 squares and each square has
13 possible states- empty, six white pieces, and six black pieces.
This works out to a one followed by only 71 zeroes, and the majority
of the states are impossible in practice.
Go has a magnitude of a googol more possible game states than chess.

## Analyzing Go Using Chess Phases

In a previous post, I wrote about using chess as a model for other games.
Go has less clearly defined phases, but the same analysis can be used.

Standard openings typically involve claiming corners or contesting a
handicap.
The board is arguably developed when rudimentary battle lines
are established at all corners and the sides of the board-
essentially all handicap locations.
The midgame begins after all major board zones have been claimed or
contested.
Therefore, a nine-stone handicap is strong because the weaker player
literally starts with a board presence everywhere.

A check could be threatening a major stone group or securing a zone of the
board.
A checkmate is a situation where the game is hopeless for the other player.
Unlike many other games, Go often ends when all locations on the board
have been played to their tactical conclusion.
The two patterns are playing to the bitter end, or playing until one player
simply concedes.

## The Brilliance of Go

Go is brilliant because deep gameplay emerges from only a single type of
game token and a board to place the tokens on.
This makes it the ultimate reduction in unnecessary complexity.
Every single rules has a very good reason for existing.

* hanicap stones allow players of different skill levels to interact
* komi balances the advantage of moving first for equal skill players
* the half point added to komi eliminates the possibility of a draw
* ko prevents endless loops that are effectively a draw
* seki and liberty counting are basic situational awareness

Many games fail to solve the above problems.

* weak players get steamrolled for poor to non-existant handicapping
* first players often have an inherent advantage that is unaccounted for
* draws are not balanced out of game scoring
* endless loops are not accounted for, and this breaks something
* many games fail to understand the implications of their own mechanics

In conclusion, Go's level of minimal design is likely inappropriate for
modern products, but its solutions to fundamental game design problems 
are absolutely worth being aware of.

