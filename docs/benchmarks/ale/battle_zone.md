---
hide:
#   - toc
  - navigation
---


# **BattleZoneNoFrameskip-v4**
## **Leaderboard**

<div>
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <table id="data-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Team ID</th>
                <th>Training Steps</th>
                <th>Params</th>
                <th>Score</th>
                <th>Code</th>
                <th>Timestamp</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>

    <script>
        $(document).ready(function() {
            const jsonFilePath = '../battle_zone.json'; // Path to your JSON file
            loadDataTable(jsonFilePath, 'data-table'); // Call the function
        });
    </script>
</div>

## **Environment Setting**
``` py
import gymnasium as gym
```