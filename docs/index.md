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
              desc: "Atari 2600 games.", 
              link: "benchmarks/ale"},
            { img: "assets/images/procgen.gif", 
              title: "Procgen", 
              desc: "Procedurally-generated environments.",
              link: "benchmarks/procgen"},
            { img: "assets/images/dmc.gif", 
              title: "DeepMind Control Suite", 
              desc: "Continuous control tasks powered by MuJoCo physics engine.",
              link: "benchmarks/dmc"},
            { img: "assets/images/minedojo.gif", 
              title: "Minedojo", 
              desc: "Open-ended exploration tasks built on Minecraft.",
              link: "benchmarks/mc"},
            { img: "assets/images/minigrid.gif", 
              title: "MiniGrid", 
              desc: "2D grid-world environments with goal-oriented tasks.",
              link: "benchmarks/mg"},
            { img: "assets/images/craftax.gif", 
              title: "Craftax", 
              desc: "A lightning-fast benchmark for open-ended RL.",
              link: "benchmarks/ct"},
            { img: "assets/images/meta-world.gif", 
              title: "Meta-World", 
              desc: "An open-source simulated benchmark for meta-RL and multi-task learning.",
              link: "benchmarks/mw"},
            { img: "assets/images/vizdoom.gif", 
              title: "ViZDoom", 
              desc: "Library for developing AI bots that play Doom using visual information.",
              link: "benchmarks/vd"},
            { img: "assets/images/smb.gif", 
              title: "Super Mario Bros", 
              desc: "Super Mario Bros on the Nintendo entertainment system.",
              link: "benchmarks/smb"},
            { img: "assets/images/d4rl.gif", 
              title: "D4RL", 
              desc: "An open-source benchmark for offline RL.",
              link: "benchmarks/d4rl"}
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
    <br>
</div>


# **Upload Your Agent**
Evaluate your excellent agent following

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
<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_polyu.svg" alt="Image 1" style="max-width: 100%; height: auto;">
  </div>
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_sjtu.svg" alt="Image 2" style="max-width: 100%; height: auto;">
  </div>
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_eias.png" alt="Image 3" style="max-width: 100%; height: auto;">
  </div>
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_idt.png" alt="Image 4" style="max-width: 100%; height: auto;">
  </div>
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_ustc.svg" alt="Image 5" style="max-width: 100%; height: auto;">
  </div>
  <div style="flex: 0 0 30%; display: flex; justify-content: center; align-items: center;">
    <img src="assets/images/logos/logo_purdue.svg" alt="Image 6" style="max-width: 100%; height: auto;">
  </div>
</div>