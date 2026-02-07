---
layout: post
mathjax: false
comments: true
title:  "Chess as a Prototypical Model for Game Progression"
date:   2023-05-17 21:05:40 +0000
categories: gamedev
---

<!-- A62 -->

Models are useful to help reason about complex problems.
This post will describe how chess can be used as a model to reason about
more complex games.
Chess will specifically be compared to Civilization 5, Magic the Gathering,
and Final Fantasy 1.

## Chess Game Scope

This session is going to cover the scope of the game of chess,
without actually going into detail on any of the rules.
Readers are expected to know the rules or know how to find them.

A chess set includes one board and 32 pieces- 16 black and 16 white.
The board is an eight by eight grid.
Squares have a rank and file.

* rank - eight horizontal rows from 1 to 8
* file - eight vertical columns from A to H

Each player gets the following six kinds of pieces.
Point values have no mechanical role, but they help players reason
about the game.

* 8 pawns (1 point each)
* 2 knights (3 points each)
* 2 bishops (3 points each)
* 2 rooks (5 points each)
* 1 queen (9 points)
* 1 king (no point value)

The rules for moving and capturing pieces are fairly simple.
In addition to learning how the different kinds of pieces move,
chess has a few special rules.

* castling
* pawn promotion
* en passant capture

There are also rules that relate to ending the game.

* check (threatened victory)
* checkmate (victory)
* stalemate (draw)
* threefold repetition rule (draw)
* resignation
* optional clock rules for competitive play

Every game starts with all pieces in predefined locations,
and white moves first.
Finally, note that chess has sufficiently few components that people
have been known to draw paper chess sets for lack of dedicated pieces.

## Chess Game Phases

If a game of chess is played from start to finish, it moves through the
following phases.

* opening
* board development
* midgame
* check
* checkmate

On the very first move,
each of the eight pawns can be moved one or two spaces,
and each of the two knights can also be moved into one of two locations.
Therefore, white can make one of twenty first moves,
and black can make one of twenty first responses.
The first move is the most important because it opens up options for
the second and subsequent moves.
Some of the first moves make more sense than others.

The opening is a set of predefined moves to start the game.
Openings can be memorized, and some are stronger than others.
Different openings lend themselves to different styles of play
and set the start of the game.
An extreme example is the two move checkmate, where
white opens F and G files and black responds with the queen for a checkmate.

Next, players focus on developing the board.
A piece is developed once it has been moved from its starting position.
The board development phase generally involves castling,
developing backrow pieces, and getting all the
non-castle side pawns into a useful formation.
Where board development starts and ends can be fuzzy, but the goal is
to get the pieces somewhere useful.
Many of the board development phase moves and responses can be memorized.

Once the board has been developed, the midgame begins.
At this point, the board is set and players can no longer rely on
having memorized exact board states and positions.
They need to use strategy and tactics to play chess.
The better player will do more damage and wind up in
a more favorable position.

A check occurs when one player threatens the other player's king.
The rules of chess dictate that a player must get their king out of
check if it is threatened.
When in check, a player's options are limited.
Sometimes this is not a problem, other times it can be used to set
up situations where the player in check loses material because
they need to focus on the king.

Simply playing better in midgame and putting the opponent's king in check
is not enough to win a game of chess.
The opponent's king must be put in a checkmate to win.
Checkmate occurs when it is impossible for the opponent to get their king
to safety.
Learning endgame checkmates is a skill that can be developed.
Depending on the circumstances, this knowledge can be used to win,
recover from a losing position,
or play for a draw.

## Chess as a Model for Other Games

Although the details depend on the title, many games move through the
same phases as chess.

* opening
* board development
* midgame
* check
* checkmate

Openings are a set of predefined moves that propel the game in one of many
directions.
They can be memorized, and people often put a lot of thought into the
analysis of openings.

The board development phase consists of collecting and deploying a
complete set of game tokens usefully.
Campaign-based games may have per-stage board development and
campaign level board development.
Note that board development often needs to occur while being
actively resisted.

The timing can be fuzzy, but at some point the board is developed, and
the player just needs to play the game.
This is the midgame.
Some games have an extremely long midgame.

A check occurs when a player threatens a victory,
or signals progress towards a victory.
Unlike chess, it may not require an immediate response.
Sometimes, however, a check does indicate a situation where one
or more players need to intervene so as not to lose the game.

A checkmate occurs when a player meets all the criteria
for a win condition.
Like chess, a checkmate often requires knowing the criteria to secure a
victory.
Midgame tactics and endgame criteria are often different,
but not unrelated.

## Civilization 5 Analysis

In Civilization 5, the opening is the initial build queue.
Many beginners tend to first build a monument.
An example of a more complex opening is scout, scout, shrine, granary,
monument, settler.
Openings can be memorized and analyzed.
Tactically, deviating from an opening rarely makes sense.

Civ 5 is far more complex than chess, but the board development phase
likely concludes around the time all early game cities have been founded
and luxury resources have been improved.
Hypothetically, cities can be founded or conquered at any time,
and tile improvements are optional, but there does tend to be a point
when cities are settled and focus shifts to playing with what is
on the board.
Note that city expansions need to be planted despite barbarians,
hostile players, and competing priorities.

The midgame consists of development and conquest that happens after the
core cities are in place.
This is the bulk of the game.
A bad initial board state can lose games, but running with a developed
board is required to win games.

Civ 5 has multiple victory conditions- score, domination, diplomacy,
science, and culture.
Score is the default win condition if the game goes on for too long without
another more specific victory condition having been met.
The other victory types have conditions that could be considered a check.

* domination - conquering the capital of another civilization
* diplomacy - having the most delegates when voting on the world leader
* science - completing the Apollo Program or attaching a spaceship part
* culture - becoming influential with another civilization

Likewise, a checkmate occurs when all the conditions for a specific
victory type have been met.

* domination - conquering the capital cities of all other civilizations
* diplomacy - having enough delegates to be voted world leader
* science - attaching all spaceship parts
* culture - becoming influential with all other civilizations

Midgame development and warfare are not enough to win the game.
Especially poor play will result in a loss, but a checkmate requires
very specific actions.

* score - playing for a high game score while not otherwise winning
* domination - systematically conquering capital cities
* diplomacy - systematically acquiring and retaining delegates
* science - researching, building and attaching spaceship parts
* culture - developing high tourism potential

Note that telegraphing a check may elicit a response from one or more
other players.
War may be declared, or an opponent may double down on their victory push.

## Magic the Gathering Analysis

Magic the Gathering (MTG) is a game where players build decks with
collectable cards.
Unlike other games, different players can show up with completely different
decks of game tokens, but the game can still be modeled using the same
chess phases.

Players draw 7 random cards at the beginning of the game, so openings
are not as reliable as chess.
Some hands are just bad.
Building a reliable deck is a skill, and certain cards will likely be
available in the first few turns if included in sufficient quantity.
Therefore, the opening consists of cards that are likely available and
playable during the first few turns of the game.

Board development largely consists of summoning creatures, but enchantments
and artifacts can also be played.
During the first few turns in a game, players will typically develop
a board to face down their opponent.

A check is any problem that threatens to kill the opponent
if left unanswered.
Even a weak 1/1 creature can be a check if the opponent has no board state.
A checkmate occurs when one player is reduced to zero life points, or an
alternate win condition is met.

The phases of chess can also be used as an analogy for collecting cards
and building decks.
Most people open with some sort of starter deck, but there are different
ways to start playing a collectible trading card game.
Board development consists of getting enough cards together to build a
competitive deck.
Check is a player's first meta deck, and checkmate is the point where
the player has the knowledge and tools to play against all the common
meta decks.

## Final Fantasy 1 Analysis

An RPG is a campaign-based game.
Each dungeon can be modelled with the chess phases, as can the
party in the context of the greater adventure.

At the campaign level, the opening is simply the player's initial party
of four heroes.
Board development consists of equipping the party, learning useful early
game spells, and maybe gaining a few levels.
The midgame consists of playing through the game after the party has a
full set of equipment.

Defeating each of the four fiends is arguably a check, and defeating the
last boss is a checkmate.
The endgame content is largely the same as the midgame content.

At the dungeon level, the opening consists of picking a direction.
Strategically approaching dungeons is possible for people who are familiar
with the game.

Board development consists of collecting key pieces of treasure.
The party keeps the gear even if a tactical retreat is necessary.
A check is any milestone that threatens to make the dungeon easy to beat,
and a checkmate is actually beating the dungeon.
Conversely, anything that threatens a party wipe could be considered a
check.

## Conclusion

Compared to modern commercial games, chess is simple and easy to reason
about.
It only has 32 pieces that are placed on a 64-square grid.
More complex games can often be broken into phases that parallel the
progression of a chess match.

* opening - actions taken immediately after starting a game
* board development - early game actions that set the stage
* midgame - the bulk of the game, tactics and strategy are used here
* check - partial victory crateria that telegraphs a win
* checkmate - complete victory criteria that scores a win
* draw - sometimes players neither win nor lose, but the game still ends
* resignation - a player can always resign if the situation is hopeless

