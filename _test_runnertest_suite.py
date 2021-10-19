import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_status(self):
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"Tokyo"))  # Enter code here
      

