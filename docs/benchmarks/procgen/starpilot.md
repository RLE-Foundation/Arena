---
hide:
  - navigation
---


# **StarPilot**
## **Hard Level**
### Leaderboard
<div>
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <table id="data-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Team</th>
                <th>Name</th>
                <th>Version</th>
                <th>Training Steps</th>
                <th>Params</th>
                <th>Score</th>
                <th>Code</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>

    <script>
        $(document).ready(function() {
            const jsonFilePath = '../../../datasets/procgen.json'; // Path to your JSON file
            const version = 'Hard';
            const environment = 'starpilot';
            loadDataTable(jsonFilePath, version, environment, 'data-table'); // Call the function
        });
    </script>
</div>

### Environment Setting
``` py
import gymnasium as gym
```

## **Easy Level**
### Leaderboard
<div>
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <table id="data-table" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Team</th>
                <th>Name</th>
                <th>Version</th>
                <th>Training Steps</th>
                <th>Params</th>
                <th>Score</th>
                <th>Code</th>
                <th>Date</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>

    <script>
        $(document).ready(function() {
            const jsonFilePath = '../../../datasets/procgen.json'; // Path to your JSON file
            const version = 'Easy';
            const environment = {starpilot};
            loadDataTable(jsonFilePath, version, environment, 'data-table'); // Call the function
        });
    </script>
</div>

### Environment Setting
``` py
import gymnasium as gym
```
