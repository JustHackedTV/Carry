from pydoc import describe
import discord, json

emojiList = json.load(open("CarryBot\DataBaseFiles\emoji.json", "r"))
guiTEXT = {
    "ZUMBI":"> **Tier 3 Revenant ** *(400k :revolving_hearts:, 120 :dagger:/s)*\n>  **Preço**: `25k`\n\n> **Tier 4 Revenant** *(1.5m :revolving_hearts:, 400 :dagger:/s)*\n> **Preço**: `100k`\n\n> **Tier 5 Revenant** *(10m :revolving_hearts:, 2'400 :dagger:/s)*\n> **Preço**: `250k`",
    "TARANTULA":"> **Tier 3 Tarantula** *(900k :revolving_hearts:, 210 :dagger:/s)*\n> **Preço**: `50k`\n\n> **Tier 4 Tarantula** *(2.4m :revolving_hearts:, 530 :dagger:/s)*\n> **Preço**: `100k`",
    "LOBO":"> **Tier 3 Sven** *(2.4m :revolving_hearts:, 180 :dagger:/s)*\n> **Preço**: `50k`\n\n> **Tier 4 Sven** *(2m :revolving_hearts:, 440 :dagger:/s)*\n> **Preço**: `125k`",
    "VOIDGLOOM":"> **Tier 1 Voidgloom** *(2.4m :revolving_hearts:, 530 :dagger:/s)*\n> **Preço**: `50k`\n\n> **Tier 2 Voidgloom** *(2.4m :revolving_hearts:, 530 :dagger:/s)*\n> **Preço**: `200k`\n\n> **Tier 3 Voidgloom** *(2.4m :revolving_hearts:, 530 :dagger:/s)*\n> **Preço**: `500k`\n\n> **Tier 4 Voidgloom** *(2.4m :revolving_hearts:, 530 :dagger:/s)*\n> **Preço**: `1m`\n> :warning: **REQUERIMENTO**: Combat 25+",
    "DEMONLORD":"\n`EM BREVE`"
}
ImagesList = {
    "ZUMBI":"https://cdn.discordapp.com/attachments/1019716902630719538/1020514171906961509/Horror.png",
    "TARANTULA":"https://cdn.discordapp.com/attachments/1019716902630719538/1020514170996805719/Broodfather.png",
    "LOBO":"https://cdn.discordapp.com/attachments/1019716902630719538/1020514172305416292/Packmaster.png",
    "VOIDGLOOM":"https://cdn.discordapp.com/attachments/1019716902630719538/1020514171487518780/Enderman.png",
    "DEMONLORD":"https://cdn.discordapp.com/attachments/1019716902630719538/1020514170451533905/Blaze.png"
}

def createCarryCommand(client, GUILDS):
    @client.command(
        name="clear",
        guild_ids=GUILDS
    )
    async def clear(ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @client.command(
        name="carry",
        description="Use este comando para criar um ticket de carry!",
        guild_ids=GUILDS
    )
    async def createCarryCmd(ctx):
        embed=discord.Embed(
            description=f"""**<:Logo:1019738501715066880> Escolha a sua carry desejada!**"""
        )
        view = discord.ui.View()

        dungeonButton = discord.ui.Button(label="Catacombs", emoji="<:Catacombs_Logo:1019731851054686228>")
        slayerButton = discord.ui.Button(label="Slayers", emoji="<:Slayers_Logo:1019734976427733002>")

        async def dungeonCallback(interaction):
            if interaction.user == ctx.author:
                embed=discord.Embed(color=0xFF0000,title="<:Catacombs_Logo:1019731851054686228> Catacombs",description=f"Aqui estão os possíveis *carrys* para a seleção **Catacombs**. Justo a elas, está aqui os seus `requerimentos`.\n\n{emojiList['BOSS']['BONZO']} **Floor 1** | *Requere Catacombs 1*\n{emojiList['BOSS']['SCARF']} **Floor 2** | *Requere Catacombs 3*\n{emojiList['BOSS']['PROFESSOR']} **Floor 3** | *Requere Catacombs 5*\n{emojiList['BOSS']['THORN']} **Floor 4** | *Requere Catacombs 9*\n{emojiList['BOSS']['LIVID']} **Floor 5** | *Requere Catacombs 14*\n{emojiList['BOSS']['SADAN']} **Floor 6** | *Requere Catacombs 19*\n{emojiList['BOSS']['NECRON']} **Floor 7** | *Requere Catacombs 24*")
                await interaction.response.edit_message(embed=embed, view=None)
        
        async def slayerCallback(interaction):
            if interaction.user == ctx.author:
                embed=discord.Embed(color=0xFFFF00,title="<:Slayers_Logo:1019734976427733002> Slayers",description=f"Aqui estão os possíveis *carrys* para a seleção **Slayers**. Justo a elas, está aqui os seus `requerimentos`.\n\n{emojiList['SLAYERS']['ZUMBI']} **Zumbi** | *Não possui Requerimento*\n{emojiList['SLAYERS']['TARANTULA']} **Tarantula** | *Matar Zumbi Tier 2*\n{emojiList['SLAYERS']['LOBO']} **Lobo** | *Matar Tarantula Tier 2*\n{emojiList['SLAYERS']['VOIDGLOOM']} **Voidgloom** | *Matar Lobo Tier 4*\n{emojiList['SLAYERS']['DEMONLORD']} **Demonlord** | *Matar Voidgloom Tier 3*")
                carryList = discord.ui.Select(placeholder="Selecione sua carry.", options=[discord.SelectOption(label="Zumbi", emoji="<:Horror:1019756161261641748>", description="Nenhum Requerimento"), discord.SelectOption(label="Tarantula", emoji="<:Broodfather:1019756158136897596>", description="Matar Zumbi Tier 2"), discord.SelectOption(label="Lobo", emoji="<:Packmaster:1019756162645770292>", description="Matar Tarantula Tier 2"), discord.SelectOption(label="Voidgloom", emoji="<:Enderman:1019756159688777758>", description="Matar Lobo Tier 4"), discord.SelectOption(label="Demonlord", emoji="<:Blaze:1019756154823381064>", description="Matar Voidgloom Tier 3")])
                async def carryListCallback(interaction):
                    if ctx.author == interaction.user:
                        embed=discord.Embed(
                            title=f"{emojiList['SLAYERS'][carryList.values[0].upper()]} {carryList.values[0]}",
                            color=0xFFFF00,
                            description=guiTEXT[carryList.values[0].upper()]
                        )
                        embed.set_thumbnail(url=ImagesList[carryList.values[0].upper()])
                        await interaction.message.delete()
                        await interaction.response.send_message(embed=embed)
                carryList.callback = carryListCallback
                view=discord.ui.View()
                view.add_item(carryList)
                await ctx.delete()
                await interaction.response.send_message(embed=embed, view=view)
        dungeonButton.callback = dungeonCallback
        slayerButton.callback = slayerCallback

        view.add_item(dungeonButton)
        view.add_item(slayerButton)

        await ctx.respond(embed=embed, view=view)
    
    @client.command(
        name="gui-test",
        guild_ids=GUILDS
    )
    async def testGUI(ctx):
        embed=discord.Embed(color=0xFFFF00,title="<:Slayers_Logo:1019734976427733002> Slayers",description=f"Aqui estão os possíveis *carrys* para a seleção **Slayers**. Justo a elas, está aqui os seus `requerimentos`.\n\n{emojiList['SLAYERS']['ZUMBI']} **Zumbi** | *Não possui Requerimento*\n{emojiList['SLAYERS']['TARANTULA']} **Tarantula** | *Matar Zumbi Tier 2*\n{emojiList['SLAYERS']['LOBO']} **Lobo** | *Matar Tarantula Tier 2*\n{emojiList['SLAYERS']['VOIDGLOOM']} **Voidgloom** | *Matar Lobo Tier 4*\n{emojiList['SLAYERS']['DEMONLORD']} **Demonlord** | *Matar Voidgloom Tier 3*")
        await ctx.respond(embed=embed)