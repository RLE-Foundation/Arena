---
hide:
  - toc
  - navigation
---

# **Arcade Learning Environment**

<div class="card-container">
    <!-- 动态生成卡片 -->
    <script>
        const cardData = [
            { img: "assets/images/atari.gif", title: "Pong", desc: "经典乒乓球游戏。", link: "./pong" },
            { img: "assets/images/atari.gif", title: "Breakout", desc: "打砖块游戏。", link: "./breakout" },
            { img: "assets/images/atari.gif", title: "Space Invaders", desc: "经典太空射击游戏。", link: "./space_invaders" },
            { img: "assets/images/atari.gif", title: "Pac-Man", desc: "经典吃豆人游戏。", link: "./pac_man" },
            { img: "assets/images/atari.gif", title: "Qbert", desc: "益智跳跃游戏。", link: "./qbert" },
            { img: "assets/images/atari.gif", title: "Seaquest", desc: "海底射击游戏。", link: "./seaquest" },
            { img: "assets/images/atari.gif", title: "Asteroids", desc: "太空射击小行星游戏。", link: "./asteroids" },
            { img: "assets/images/atari.gif", title: "Ms. Pac-Man", desc: "吃豆人变种游戏。", link: "./ms_pac_man" },
            { img: "assets/images/atari.gif", title: "Montezuma's Revenge", desc: "冒险解谜游戏。", link: "./montezumas_revenge" },
            { img: "assets/images/atari.gif", title: "Enduro", desc: "赛车竞速游戏。", link: "./enduro" },
            { img: "assets/images/atari.gif", title: "Frostbite", desc: "冰雪冒险游戏。", link: "./frostbite" },
            { img: "assets/images/atari.gif", title: "River Raid", desc: "空中射击游戏。", link: "./river_raid" }
        ];

        const cardContainer = document.querySelector('.card-container');

        cardData.forEach(data => {
            const card = document.createElement('a');
            card.className = 'env_card';
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