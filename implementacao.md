✅ Escopo já implementado:
Cadastro e login de usuários

Relacionamento com nome do casal

Página de conversa com mensagens estilo WhatsApp

Armazenamento de mensagens no banco

Sessões de usuário

Visual agradável com estilização topzera

🌱 Evolução do Software — Amorzinho Rede
🧩 Funcionalidade: Expiração de Mensagens e Desbloqueio de Benefícios Premium
🎯 Objetivo Geral
Melhorar a experiência dos usuários de longa data, recompensando a continuidade e o uso frequente do app. Ao mesmo tempo, manter o banco de dados limpo, removendo automaticamente mensagens antigas.

🛠️ Funcionalidades a serem implementadas

1. Validade das Mensagens
   Toda mensagem enviada terá uma "data de criação" registrada automaticamente.

A partir dessa data, será considerada válida por 30 dias.

2. Exclusão Automática
   Ao acessar o app (página de conversa), o sistema irá verificar e excluir mensagens que já passaram da validade.

Esse processo será transparente para o usuário.

3. Sistema de Reconhecimento Premium
   Quando for detectado que o relacionamento completou 30 dias de existência, o sistema exibirá:

Um selo comemorativo premium

Um texto de incentivo ("Vocês estão juntos há mais de 30 dias! 💖")

A possibilidade de desbloquear um novo visual ou funcionalidade exclusiva

4. Estímulo ao Engajamento
   O selo e os recursos desbloqueados funcionam como recompensa afetiva, valorizando o tempo de relação.

Reforça a ideia de que o relacionamento e o app evoluem juntos.

✨ Recompensas Visuais Premium
Essas recompensas podem incluir:

Novos temas de cores (ex: rosinha pastel, tema estrelado, etc.)

Stickers ou emojis exclusivos dentro das mensagens

Animações de entrada no app (tipo corações flutuando ao abrir)

Um mini mural com "momentos especiais" (mensagens fixadas)

🧠 Considerações Técnicas
A lógica de exclusão será executada no backend com base na data de criação de cada mensagem.

O tempo de relacionamento será calculado pela data de criação do relacionamento registrada no banco.

O frontend será adaptado para mostrar elementos visuais condicionais (selo, tema, animações), com base nos dados recebidos do backend.
