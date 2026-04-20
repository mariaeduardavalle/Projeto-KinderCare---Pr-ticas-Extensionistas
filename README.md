# KinderCare+

Sistema web em Django para controle de presença e gestão de terapias da instituição, substituindo papel e Excel por um processo centralizado.

## Tecnologias
- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- WhiteNoise para arquivos estáticos
- GitHub
- Vercel (arquivo base incluído, mas o foco do projeto está no backend)

## Módulos implementados
- Usuários e acesso com perfis (`recepcao`, `terapeuta`, `coordenacao`)
- Pacientes
- Terapeutas e especialidades
- Agenda semanal fixa
- Geração de atendimentos do período
- Controle de presença
- Atendimentos extras (encaixes)
- Evoluções clínicas
- Relatórios de produtividade
- Dashboard pós-login com menu de módulos

## Regras de acesso
- **Coordenação:** acesso total, incluindo usuários e relatórios
- **Recepção:** pacientes, terapeutas, agenda, presença e extras
- **Terapeuta:** visualização dos próprios atendimentos, presença, extras e evoluções dos seus pacientes

## Como rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Fluxo principal
1. Coordenação cadastra usuários e perfis.
2. Recepção/coordenação cadastra pacientes e terapeutas.
3. Coordenação/recepção monta a agenda semanal fixa.
4. O sistema gera os atendimentos do período.
5. Recepção ou terapeuta registra presença.
6. Terapeuta registra a evolução clínica.
7. Coordenação acompanha a produtividade por período.
