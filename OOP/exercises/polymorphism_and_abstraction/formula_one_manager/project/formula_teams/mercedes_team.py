from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    PETRONAS = {
        1: 1_000_000,
        2: 500_000,
        3: 500_000,
    }

    TEAM_VIEWER = {
        1: 100_000,
        2: 100_000,
        3: 100_000,
        4: 100_000,
        5: 100_000,
        6: 50_000,
        7: 50_000
    }


    def calculate_revenue_after_race(self, race_pos: int):
        petronas_bonus = self.PETRONAS.get(race_pos) if self.PETRONAS.get(race_pos) else 0
        team_viewer_bonus = self.TEAM_VIEWER.get(race_pos) if self.TEAM_VIEWER.get(race_pos) else 0

        revenue = petronas_bonus + team_viewer_bonus - 200_000

        self.budget += revenue

        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"