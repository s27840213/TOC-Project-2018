# from bottle import route, run, request, abort, static_file
from bottle import route, run, request, abort, static_file

from fsm import TocMachine

#EAAG2a0mVCxkBAOAtOoutGZBvXkKbrzReE6TZB5LcBg7XG652WJtMkTP1IaFZCTG7Pz86qGJ2bqkgvITGcXe8xZCn3GzFKiFGs6qhaRM7O99N3f56lDufWD2xH0EFCxBiZCvGE6xPIxZBiLl4UOZAKMl4RCkYVGJW3PXRKE7cxkuGAZDZD
VERIFY_TOKEN = "EAAG2a0mVCxkBAHwSDiL9UQggacpBN5WZBpOegMeEuM4C6096ehWdYeeW5gZBYK6VizqiE2ZAnpYZAgD7cOIiMsbgYSEAE293eZCpVEWMvTMoS0EwZCf6oZCLimK3nzNQZASYdEdSUAd3uIr2HR8J8eTTSqztZCCps5Gh0eWHlT6lxXwZDZD"
machine = TocMachine(
    states=[
        'init',
        'user',
        'askMemb',
        'askRecord',
        'showMembInfo',
        'funPhoto'
    ],
    transitions=[
        {
            'trigger':'advance',
            'source': 'init',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'askMemb',
            'conditions': 'is_going_to_askMemb'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'askRecord',
            'conditions': 'is_going_to_askRecord'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'funPhoto',
            'conditions': 'is_going_to_funPhoto'
        },
        #         {
        #     'trigger': 'advance',
        #     'source': 'funPhoto',
        #     'dest': 'funPhoto',
        #     'conditions': 'is_going_to_funPhoto'
        # },        
        {
            'trigger': 'advance',
            'source': 'askMemb',
            'dest': 'showMembInfo',
            'conditions': 'is_going_to_showMembInfo'
        },
        {
            'trigger': 'advance',
            'source': 'showMembInfo',
            'dest': 'showMembInfo',
            'conditions': 'is_going_to_showMembInfo'
        },
        {
            'trigger': 'go_back',
            'source': [
                'askMemb',
                'askRecord',
                'showMembInfo',
                'funPhoto'
            ],
            'dest': 'init'
        }
    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
