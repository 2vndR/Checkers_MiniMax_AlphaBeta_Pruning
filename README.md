# Checkers_MiniMax_AlphaBeta_Pruning
## Checkers game with MiniMax algorithm, added Alpha Beta Pruning. Originally made by https://www.youtube.com/@TechWithTim

I found a way to fix a bug in the original repository. After making the piece a King, it would start trying to increase the King counter everytime by moving back and forth to the goal row, instead of trying to capture enemy pieces. Just had to add a line to make it so the counter does not increase when the piece is already crowned.
