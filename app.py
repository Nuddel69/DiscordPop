from interactions import Client, slash_command, SlashContext, slash_option, OptionType
import json

token = json.load(open('secret.json'))["token"]

bot = Client(token=token)

@slash_command(name="hi", description="Greetings")
async def hi_function(ctx: SlashContext):
    await ctx.send("Hello World")

@slash_command(name='pop', description="Bubblewrap!")
@slash_option(
    name="dimensions",
    description="Bubblewrap size. Syntax: '<width>x<height>'",
    required=True,
    opt_type=OptionType.STRING
)
async def bubble(ctx: SlashContext, dimensions: str):
    bubbles = ''
    dimensions = dimensions.split('x')
    width = int(dimensions[0])
    height = int(dimensions[1])

    for i in range(height):
        for i in range(width):
            bubbles = bubbles + '||pop||'
        bubbles = bubbles + '\n'

    if len(bubbles) < 2000:
        message = await ctx.send(bubbles)
        await message.add_reaction('🔄')
    else:
        await ctx.send("That's too big of a bubblewrap, you wouldn't be able to pop them all!")

bot.start()
