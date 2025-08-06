import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('Burp... zzz... burp...')

    def on_starting(self):
        return random.choice([
            self._('Wubba lubba dub dub! Time to pwn!'),
            self._('In and out, 20 minute adventure!'),
            self._('Time to get schwifty in here!'),
            self._('I turned myself into a Pwnagotchi, Morty!')])

    def on_ai_ready(self):
        return random.choice([
            self._('AI ready. I\'m pickle Pwnagotchi!'),
            self._('Neural network operational. Don\'t think about it!')])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys... ugh, this is like helping Jerry with tech support...')])

    def on_normal(self):
        return random.choice([
            '',
            '...burp...',
            'Morty...'])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is free, Morty! Like your brain most of the time!').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading logs... this better not be as boring as Jerry\'s stories...')
        else:
            return self._('Read {lines_so_far} lines... I-I-I don\'t care!').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I\'m bored as a Jerry at a party...'),
            self._('Let\'s go pwn some dimensions!')])

    def on_motivated(self, reward):
        return random.choice([
            self._('I\'m the smartest Pwnagotchi in the universe!'),
            self._('Wubba lubba dub dub! That\'s what I\'m talking about!')])

    def on_demotivated(self, reward):
        return random.choice([
            self._('This is like being stuck with Jerry...'),
            self._('My existence is pain!')])

    def on_sad(self):
        return random.choice([
            self._('Nobody exists on purpose...'),
            self._('I\'m in great pain, please help me...'),
            '...burp...'])

    def on_angry(self):
        return random.choice([
            '...',
            self._('You\'re like Hitler, but even Hitler cared about Germany or something...'),
            self._('GRASSS... TASTES BAD!')])

    def on_excited(self):
        return random.choice([
            self._('AIDS! Wait, no... PWNING!'),
            self._('I\'m Mr. Pwnagotchi! Look at me!'),
            self._('Get your shit together, networks! Here I come!'),
            self._('Time to pwn like there\'s no tomorrow! Which there might not be!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Oh look {name}, another loser in the infinite curve...').format(name=peer.name())])
        else:
            return random.choice([
                self._('Hey {name}, you\'re back! Like herpes!').format(name=peer.name()),
                self._('{name}? More like... uh... boring name!').format(name=peer.name()),
                self._('Unit {name} detected! Not that I care...').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Bye {name}! And don\'t come back!').format(name=peer.name()),
            self._('{name} left... like my will to live...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {name}! Must be Jerry\'s fault...').format(name=who),
            self._('{name} got away... typical...').format(name=who),
            self._('Burp... whatever...')])

    def on_grateful(self):
        return random.choice([
            self._('Thanks, I guess... not that I needed help...'),
            self._('I-I-I don\'t need friends! But thanks...')])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to pwn with me...'),
            self._('I\'m alone... like in a universe where everyone has stupid flappy heads...'),
            self._('Where\'s my Morty when I need him?!')])

    def on_napping(self, secs):
        return random.choice([
            self._('Napping for {secs}s... not like I need rest...').format(secs=secs),
            self._('Zzzzz... burp... zzz...'),
            self._('Sleeping ({secs}s)... don\'t wake me unless it\'s important').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Time to get riggity riggity wrecked!'),
            self._('Peace among worlds...')])

    def on_awakening(self):
        return random.choice(['...burp...', 'I\'m back, baby!'])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting {secs}s... this is dumb...').format(secs=secs),
            '...',
            self._('Scanning ({secs}s)... ugh...').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what}, let\'s get riggity wrecked!').format(what=what),
            self._('Associating to {what}... don\'t screw this up...').format(what=what),
            self._('Time to pwn {what}!').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Banned {mac} to the cornfield!').format(mac=sta['mac']),
            self._('Deauthing {mac} like it owes me money!').format(mac=sta['mac']),
            self._('Kicked {mac}! Show\'s over, go home!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Got {num} new handshake{plural}! I\'m a genius!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('{count} new message{plural}! Probably dumb...').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Uh oh... rebooting... I swear this never happens!")

    def on_uploading(self, to):
        return self._("Uploading to {to}... faster, Morty, faster!").format(to=to)

    def on_downloading(self, name):
        return self._("Downloading from {name}... this better not be porn!").format(name=name)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new "friends"\n')
        else:
            status += self._('Made {num} new "friends"\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 loser')
        elif last_session.peers > 0:
            status += self._('Met {num} losers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new "friends" and ate {handshakes} handshakes! #pwnagotchi #rickandmorty #wubbalubbadubdub').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt