'''
Updated March 5, 2021

@author: Chloe Quinto
@class: SSW 567 - HW 4

Unit Test for Github API

I pledge my honor that I have abided by the Stevens Honor System - Chloe Quinto

NOTE: As of 3/6/21, the [*]_result variables are accurate. They are subject to change
over time.
'''
import unittest

from main import retrieve_user_repos, retrieve_commits

CQ_RESULT = """
Repo: Applied-Machine-Learning Number of commits 38
Repo: Bok_Bok_Pox Number of commits 8
Repo: code-base-metrics Number of commits 24
Repo: COVID-19-LSTM Number of commits 10
Repo: CPE-390-Microprocessor-Systems Number of commits 35
Repo: CPE-487-Digital-System-Design Number of commits 6
Repo: CPE345_FinalProject Number of commits 30
Repo: CPE_360_Files Number of commits 8
Repo: Crypto Number of commits 11
Repo: CS115 Number of commits 33
Repo: DA-projects Number of commits 16
Repo: Deep-Learning Number of commits 17
Repo: DeepLearning Number of commits 6
Repo: EncodeFlix Number of commits 23
Repo: EVE_online Number of commits 83
Repo: film_locations_gmap Number of commits 4
Repo: GithubApi567 Number of commits 3
Repo: guides Number of commits 100 or more
Repo: ImgProc Number of commits 49
Repo: InfoSys Number of commits 2
Repo: OnlineSocialNetworks Number of commits 27
Repo: react-navbar-dropdown Number of commits 1
Repo: Resume Number of commits 2
Repo: SSW_555_Project Number of commits 100 or more
Repo: StevensMarketplace Number of commits 74
Repo: stevens_library_seating Number of commits 10
Repo: tracerouteViz Number of commits 38
Repo: Twitter-Giveaway-Bot Number of commits 36
""".strip()

RK_RESULTS = """
Repo: csp Number of commits 2
Repo: hellogitworld Number of commits 50
Repo: helloworld Number of commits 6
Repo: Mocks Number of commits 10
Repo: Project1 Number of commits 2
Repo: richkempinski.github.io Number of commits 9
Repo: threads-of-life Number of commits 1
Repo: try_nbdev Number of commits 2
Repo: try_nbdev2 Number of commits 5
""".strip()

CIRO_RESULTS = """
Repo: -21- Number of commits 1
Repo: 2047 Number of commits 100 or more
Repo: 21- Number of commits 2
Repo: 996.BROWSER Number of commits 19
Repo: 996.ICU Number of commits 100 or more
Repo: aarch64-bare-metal-qemu Number of commits 11
Repo: adventures_in_opencl Number of commits 98
Repo: algorithm-cheat Number of commits 82
Repo: algorithms Number of commits 24
Repo: algorithms-fork Number of commits 100 or more
Repo: AlgorithmsSedgewick Number of commits 12
Repo: AlgoXY-fork Number of commits 100 or more
Repo: all-github-commit-emails Number of commits 22
Repo: android-cheat Number of commits 71
Repo: android-vulkan-tutorials Number of commits 16
Repo: Apertus Number of commits 100 or more
Repo: arm-assembly-cheat Number of commits 100 or more
Repo: arm-doom Number of commits 9
Repo: arm-sandbox Number of commits 38
Repo: arm-trusted-firmware Number of commits 100 or more
Repo: armv8-bare-metal Number of commits 22
Repo: arsane.github.io Number of commits 100 or more
Repo: asciidoctor Number of commits 100 or more
Repo: asciidoctor-katex Number of commits 37
Repo: asciidoctor-katex-2 Number of commits 9
Repo: ASIC Number of commits 13
Repo: atom Number of commits 100 or more
Repo: awesome-china Number of commits 24
Repo: awesome-china-media Number of commits 12
Repo: awesome-reinforcement-learning-games Number of commits 54
Repo: awesome-reverse-engineering Number of commits 3
... User has more than 30 public repos
""".strip()

class TestGithub(unittest.TestCase):
    '''
    Defines multiple sets of test cases
    '''
    def test_http_errors_for_users(self):
        '''
        Checks for HTTP Errors for Users
        '''
        self.assertEqual(retrieve_user_repos("cholequinto"), "ERROR: Status code for user: 404")

    def test_http_errors_for_repos(self):
        '''
        Checks for HTTP Errors for Repos
        '''
        self.assertEqual(retrieve_commits("chloequinto", "nonexistantrepo"), \
            "ERROR: Status code for repo: 404")

    def test_bad_input(self):
        '''
        Checks for inputs that are not strings
        '''
        self.assertEqual(retrieve_user_repos(12), "Invalid Input")
        self.assertEqual(retrieve_user_repos(3454.222), "Invalid Input")
        self.assertEqual(retrieve_user_repos(True), "Invalid Input")

    def test_repo(self):
        '''
        Checks for correct response from specific users
        '''
        self.assertEqual(retrieve_user_repos("chloequinto").strip(), CQ_RESULT)
        self.assertEqual(retrieve_user_repos("richkempinski").strip(), RK_RESULTS)

    def test_commits(self):
        '''
        Checks specific commit by users
        '''
        self.assertEqual(retrieve_commits("chloequinto", "Applied-Machine-Learning"), 38)
        self.assertEqual(retrieve_commits("chloequinto", "StevensMarketplace"), 74)
        self.assertEqual(retrieve_commits("richkempinski", "hellogitworld"), 50)
        self.assertEqual(retrieve_commits("richkempinski", "threads-of-life"), 1)

    def test_over_100_commits(self):
        '''
        Checks for over 100 commits for a repo
        '''
        self.assertEqual(retrieve_commits("cirosantilli", "test-many-commits-1m"), "100 or more")

    def test_over_100_user_repos(self):
        '''
        Checks for users that have more than 30 repos
        '''
        self.assertEqual(retrieve_user_repos("cirosantilli").strip(), CIRO_RESULTS)

    def test_zero_user_repos(self):
        '''
        Checks for users with no repos
        '''
        self.assertEqual(retrieve_user_repos("guandicimo"), "User has no public repos")

if __name__ == "__main__":
    print("Running Unit Tests")
    unittest.main(verbosity=0)
