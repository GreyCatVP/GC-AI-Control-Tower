<!-- ЗАМЕНИ `username` на свой GitHub-логин. Положи все изображения в папку assets/ этого же репозитория. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/projects-banner-dark.png">
  <img src="assets/projects-banner-light.png" alt="Grey Cat — проекты и MVP" width="100%">
</picture>

---

### Привет! Я Влад — делаю живых AI‑аватаров брендов, RAG‑инструменты и лёгкие MVP под бизнес‑процессы.

**Фокус:** бренд‑аватары · RAG + FinOps · AI‑ассистенты · TG‑боты · визуальные пайплайны · приватность/политики.

---

## Проекты (быстрые ссылки)

<table>
  <tr>
    <td>
      <a href="https://github.com/username/ai-brand-avatar">
        <img src="assets/ai-brand-avatar.png" alt="AI Brand Avatar" width="360"><br>
        <sub><b>AI Brand Avatar</b> — голос бренда (TG + API)</sub>
      </a>
    </td>
    <td>
      <a href="https://github.com/username/rag-finder-mini">
        <img src="assets/rag-finder-mini.png" alt="RAG Finder Mini" width="360"><br>
        <sub><b>RAG Finder Mini</b> — быстрый поиск с Top‑K/дедупом</sub>
      </a>
    </td>
    <td>
      <a href="https://github.com/username/greycat-lora-trainer">
        <img src="assets/greycat-lora-trainer.png" alt="GreyCat‑LoRA Trainer" width="360"><br>
        <sub><b>GreyCat‑LoRA Trainer</b> — дообучение SD1.5/SDXL</sub>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/username/voiceofbrandbot">
        <img src="assets/voiceofbrandbot.png" alt="VoiceOfBrandBot" width="360"><br>
        <sub><b>VoiceOfBrandBot</b> — универсальный TG‑бот бренда</sub>
      </a>
    </td>
    <td>
      <a href="https://github.com/username/data-governance-privacy-ai-layer">
        <img src="assets/data-governance.png" alt="Data Governance & Privacy AI‑layer" width="360"><br>
        <sub><b>Data Governance & Privacy</b> — политики/маскирование/лог</sub>
      </a>
    </td>
    <td>
      <a href="https://github.com/username/ai-control-tower">
        <img src="assets/ai-control-tower.png" alt="AI Control Tower" width="360"><br>
        <sub><b>AI Control Tower</b> — cost/risk/access на одном экране</sub>
      </a>
    </td>
  </tr>
</table>

> Если на тёмной теме миниатюры «проваливаются» — добавь версии `*-dark.png` и смени `<img ...>` на `<picture>` по аналогии с баннером.

---

## Быстрый старт (как повторить демо локально)

```bash
# 1) Клонировать любой проект
git clone https://github.com/username/ai-brand-avatar && cd ai-brand-avatar

# 2) Создать окружение и зависимости
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3) Заполнить .env (ключи/токены)
cp -n .env.example .env && nano .env

# 4) Запуск (пример для бота)
python bot.py
```

---

### Контакты

* Telegram: **@your\_handle**
* Email: **[you@example.com](mailto:you@example.com)**

<sub>Баннер/превью: 1920×480 (2×: 3840×960). Миниатюры: \~720×420 (2×: 1440×840). Держи ассеты в этом же репо для стабильной загрузки.</sub>
