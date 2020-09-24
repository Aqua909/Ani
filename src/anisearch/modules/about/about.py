import platform
from datetime import timedelta
from time import time

import discord
import psutil
from discord.ext import commands

import main


class About(commands.Cog, name='About'):

    def __init__(self, client):
        self.client = client

    @commands.command(name='about', usage='about', brief='3s', ignore_extra=False)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cmd_about(self, ctx):
        """Displays information and stats about the bot."""
        about_embed = discord.Embed(title='About %s' % self.client.user.name,
                                    description='<@!%s> is an easy-to-use Discord bot that allows you to search for '
                                                'Anime, Manga, Characters, Staff, Studios and Profiles right within '
                                                'Discord!\n\n If you have any suggestions use `contact <message>` or '
                                                'add me as a friend.' % self.client.user.id,
                                    color=0x4169E1, timestamp=ctx.message.created_at)
        about_embed.add_field(name='❯ Creator', value='<@!%s>' % main.__owner_id__,
                              inline=True)
        about_embed.add_field(name='❯ Version', value='v%s' % main.__version__,
                              inline=True)
        about_embed.add_field(name='❯ Commands', value='as!help',
                              inline=True)
        proc = psutil.Process()
        with proc.oneshot():
            uptime = timedelta(seconds=round(time() - proc.create_time()))
        try:
            about_embed.add_field(name='❯ Uptime', value=str(uptime), inline=True)
        except AttributeError:
            about_embed.add_field(name='❯ Uptime', value='-',
                                  inline=True)
        about_embed.add_field(name='❯ Guilds', value=str(len(self.client.guilds)),
                              inline=True)
        about_embed.add_field(name='❯ Users', value=str(len(self.client.users)),
                              inline=True)
        about_embed.add_field(name='❯ Library', value='Discord.py',
                              inline=True)
        about_embed.add_field(name='❯ Python version', value='v%s' % platform.python_version(),
                              inline=True)
        about_embed.add_field(name='❯ Invite', value='[Click me!](%s)' % main.__invite__,
                              inline=True)
        about_embed.add_field(name='❯ Vote', value='[Click me!](%s)' % main.__vote__,
                              inline=True)
        about_embed.set_thumbnail(url=self.client.user.avatar_url)
        about_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=about_embed)


def setup(client):
    client.add_cog(About(client))
    main.logger.info('Loaded extension About')


def teardown():
    main.logger.info('Unloaded extension About')
