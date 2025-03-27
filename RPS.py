def player(prev_play, opponent_history=[]):
    # Inicializa o histórico se for o primeiro jogo
    if not prev_play:
        opponent_history.clear()
        return "R"
    
    # Adiciona a última jogada do oponente ao histórico
    opponent_history.append(prev_play)
    
    # Se tivermos menos de 5 jogadas, jogue aleatoriamente
    if len(opponent_history) < 5:
        return "RPS"[len(opponent_history) % 3]
    
    # Analisa as últimas jogadas do oponente para encontrar padrões
    last_five = "".join(opponent_history[-5:])
    
    # Dicionário para contar as jogadas após cada sequência de 4 jogadas
    patterns = {}
    for i in range(len(opponent_history)-4):
        sequence = "".join(opponent_history[i:i+4])
        next_move = opponent_history[i+4]
        if sequence in patterns:
            if next_move in patterns[sequence]:
                patterns[sequence][next_move] += 1
            else:
                patterns[sequence][next_move] = 1
        else:
            patterns[sequence] = {next_move: 1}
    
    # Pega a última sequência de 4 jogadas
    current_sequence = last_five[-4:]
    
    if current_sequence in patterns:
        # Prevê a próxima jogada mais provável do oponente
        prediction = max(patterns[current_sequence].items(), 
                        key=lambda x: x[1])[0]
        
        # Escolhe a jogada que vence a previsão
        if prediction == "R":
            return "P"
        elif prediction == "P":
            return "S"
        else:
            return "R"
    
    # Se não encontrar padrão, joga baseado na última jogada do oponente
    if prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    else:
        return "R" 
