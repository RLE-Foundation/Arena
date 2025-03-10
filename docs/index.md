---
hide:
  - toc
---


# **Leaderboard**


<div class="card-container">
    <!-- 动态生成卡片 -->
    <script>
        const cardData = [
            { img: "assets/images/atari.gif", 
              title: "Arcade Learning Environment", 
              desc: "这是第一个卡片的简短说明。", 
              link: "benchmarks/ale"},
            { img: "assets/images/procgen.png", 
              title: "Procgen", 
              desc: "这是第二个卡片的简短说明。",
              link: "benchmarks/procgen"},
            { img: "assets/images/dmc.png", 
              title: "DeepMind Control Suite", 
              desc: "这是第三个卡片的简短说明。",
              link: "benchmarks/dmc"},
            { img: "assets/images/mc.webp", 
              title: "Minecraft", 
              desc: "这是第四个卡片的简短说明。",
              link: "benchmarks/mc"}
        ];

        const cardContainer = document.querySelector('.card-container');

        cardData.forEach(data => {
            const card = document.createElement('a');
            card.className = 'card';
            card.href = data.link;
            card.target = "_self";

            card.innerHTML = `
                <img src="${data.img}" alt="">
                <div class="card-content">
                    <h2>${data.title}</h2>
                    <p>${data.desc}</p>
                </div>
            `;

            cardContainer.appendChild(card);
        });
    </script>
</div>

---


# **Upload Your Agent**


# **Cite Us**
If you use **RLLTE Arena** in your research, please cite this project like this:
```bibtex
@article{yuan2025arena,
  title={Arena}, 
  author={Mingqi Yuan and Qi Wang and Bo Li and Xin Jin and Wenjun Zeng},
  year={2025},
  journal={arXiv preprint arXiv:}
}
```

# **Powered by**
