import sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = r'c:\Users\Chaerul Azriel A\OneDrive\Pictures\Figma\index.html'

HTML_HEAD = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Honkai: Web Rail</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark:#0b0f19; --panel-bg:rgba(20,25,40,0.85);
            --primary-gold:#d4af37; --accent-blue:#00d2ff;
            --danger-red:#ff4b4b; --heal-green:#4caf50; --shield-white:#87cefa;
            --energy-yellow:#ffeb3b; --jade-pink:#ff66cc; --debuff-purple:#9370db;
            --target-glow:0 0 15px rgba(212,175,55,0.8);
        }
        *{box-sizing:border-box;margin:0;padding:0;}
        body{background:radial-gradient(circle at top right,#1a2235,#0b0f19);color:white;font-family:\'Rajdhani\',sans-serif;overflow-x:hidden;}
        h1,h2,h3{font-family:\'Orbitron\',sans-serif;color:var(--primary-gold);}
        .spa-view{display:none;min-height:100vh;padding:15px;}
        .active-view{display:block;}
        .glass-panel{background:var(--panel-bg);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:20px;box-shadow:0 0 10px rgba(0,210,255,0.2);backdrop-filter:blur(10px);}
        .hsr-btn{background:linear-gradient(45deg,#111,#222);border:1px solid var(--primary-gold);color:var(--primary-gold);padding:8px 15px;font-family:\'Orbitron\';font-size:13px;cursor:pointer;border-radius:4px;transition:0.2s;text-transform:uppercase;font-weight:bold;}
        .hsr-btn:hover:not(:disabled){background:var(--primary-gold);color:#000;box-shadow:0 0 15px var(--primary-gold);}
        .hsr-btn.blue{border-color:var(--accent-blue);color:var(--accent-blue);}
        .hsr-btn.blue:hover:not(:disabled){background:var(--accent-blue);color:#000;box-shadow:0 0 15px var(--accent-blue);}
        .hsr-btn.ult{border-color:var(--primary-gold);color:var(--primary-gold);}
        .hsr-btn:disabled{opacity:0.4;cursor:not-allowed;border-color:#555;color:#777;background:#222;box-shadow:none;}
        .hsr-input{width:100%;padding:12px;margin-bottom:15px;background:rgba(0,0,0,0.5);border:1px solid var(--accent-blue);color:white;border-radius:4px;}
        .navbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.1);}
        .modal-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);z-index:1000;justify-content:center;align-items:center;}
        .modal-overlay.active{display:flex;}
        .modal-content{background:var(--bg-dark);border:1px solid var(--primary-gold);border-radius:8px;padding:20px;width:95%;max-width:450px;text-align:center;box-shadow:0 0 20px rgba(212,175,55,0.4);max-height:90vh;overflow-y:auto;}
        .modal-content img{width:100px;height:100px;border-radius:8px;border:2px solid var(--accent-blue);margin-bottom:10px;object-fit:cover;}
        .eidolon-list{text-align:left;font-size:11px;background:#111;padding:10px;border-radius:6px;margin-bottom:15px;color:#ccc;border:1px solid #333;}
        .eidolon-item{margin-bottom:5px;}
        .eidolon-item.active{color:var(--primary-gold);font-weight:bold;}
        .char-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:12px;margin-top:15px;max-height:65vh;overflow-y:auto;padding-right:10px;}
        .char-grid::-webkit-scrollbar{width:8px;}
        .char-grid::-webkit-scrollbar-track{background:#111;border-radius:4px;}
        .char-grid::-webkit-scrollbar-thumb{background:var(--accent-blue);border-radius:4px;}
        .char-card-select{border:1px solid #444;border-radius:8px;padding:8px;text-align:center;cursor:pointer;transition:0.3s;background:rgba(0,0,0,0.6);position:relative;overflow:hidden;}
        .char-card-select:hover{border-color:var(--accent-blue);transform:translateY(-4px);}
        .char-card-select.selected{border-color:var(--primary-gold);box-shadow:var(--target-glow);background:rgba(212,175,55,0.1);}
        .char-card-select.locked{filter:grayscale(100%) brightness(0.4);border-color:#222;}
        .char-img{width:75px;height:75px;border-radius:5px;border:2px solid #555;margin-bottom:4px;object-fit:cover;background:#111;}
        .role-badge{position:absolute;top:4px;right:4px;font-size:8px;padding:2px 4px;border-radius:3px;background:#222;border:1px solid #fff;font-weight:bold;z-index:2;}
        .eidolon-badge{position:absolute;top:4px;left:4px;font-size:9px;padding:2px 4px;border-radius:3px;background:var(--primary-gold);color:#000;font-weight:bold;z-index:2;}
        .battle-wrapper{display:flex;flex-direction:column;gap:20px;}
        @media(min-width:900px){.battle-wrapper{flex-direction:row;justify-content:space-between;}}
        .team-container{flex:1;display:flex;flex-direction:column;gap:10px;}
        .enemy-container{align-items:flex-end;}
        .entity-card{border-radius:6px;border:1px solid #333;background:rgba(0,0,0,0.6);display:flex;align-items:center;gap:10px;padding:10px;width:100%;max-width:400px;position:relative;transition:0.2s;}
        .entity-card.active-turn{border-color:var(--accent-blue);box-shadow:0 0 15px rgba(0,210,255,0.5);transform:scale(1.02);z-index:10;background:rgba(0,210,255,0.1);}
        .entity-card.enemy{cursor:pointer;}
        .entity-card.enemy:hover{border-color:var(--danger-red);}
        .entity-card.enemy.targeted{border-color:var(--primary-gold);box-shadow:var(--target-glow);transform:scale(1.02);}
        .entity-card.dead{opacity:0.3;filter:grayscale(100%);pointer-events:none;}
        .entity-img{width:55px;height:55px;border-radius:6px;border:1px solid #555;object-fit:cover;background:#111;}
        .info-box{flex:1;position:relative;}
        .bar-container{width:100%;height:10px;background:#222;border-radius:5px;margin:5px 0 2px;overflow:hidden;border:1px solid #444;position:relative;}
        .hp-bar{height:100%;background:var(--heal-green);transition:width 0.3s;position:absolute;z-index:1;}
        .hp-bar.enemy-bar{background:var(--danger-red);}
        .shield-bar{height:100%;background:var(--shield-white);transition:width 0.3s;position:absolute;z-index:2;opacity:0.8;}
        .energy-container{width:100%;height:4px;background:#222;border-radius:2px;overflow:hidden;margin-bottom:5px;}
        .energy-bar{height:100%;background:var(--energy-yellow);transition:width 0.3s;}
        .status-tray{display:flex;gap:3px;margin-top:2px;height:14px;}
        .status-icon{font-size:10px;background:rgba(0,0,0,0.8);padding:1px 4px;border-radius:3px;border:1px solid #666;}
        .sp-wrapper{display:flex;align-items:center;justify-content:center;gap:5px;margin-bottom:10px;}
        .sp-dot{width:15px;height:15px;border-radius:50%;border:1px solid var(--primary-gold);background:#222;transition:0.3s;}
        .sp-dot.active{background:var(--primary-gold);box-shadow:0 0 8px var(--primary-gold);}
        .dmg-popup{position:absolute;font-weight:bold;font-size:26px;font-family:\'Orbitron\';text-shadow:2px 2px 0 #000,-2px -2px 0 #000,2px -2px 0 #000,-2px 2px 0 #000;animation:popAnim 0.8s forwards;z-index:100;pointer-events:none;top:10px;left:50%;transform:translateX(-50%);}
        @keyframes popAnim{0%{opacity:1;transform:translate(-50%,0) scale(0.5);}20%{transform:translate(-50%,-20px) scale(1.2);}100%{opacity:0;transform:translate(-50%,-50px) scale(1);}}
        @keyframes atk-anim{0%,100%{transform:translateX(0);}50%{transform:translateX(25px);}}
        @keyframes atk-anim-enemy{0%,100%{transform:translateX(0);}50%{transform:translateX(-25px);}}
        @keyframes dmg-anim{0%,100%{transform:translateX(0);filter:brightness(1);}25%{transform:translateX(-5px);filter:brightness(1.5) drop-shadow(0 0 10px red);}75%{transform:translateX(5px);}}
        @keyframes heal-anim{0%,100%{transform:translateY(0);}50%{filter:drop-shadow(0 0 15px var(--heal-green));transform:translateY(-8px);}}
        @keyframes buff-anim{0%,100%{transform:scale(1);}50%{filter:drop-shadow(0 0 15px var(--primary-gold));transform:scale(1.05);}}
        .is-attacking{animation:atk-anim 0.3s ease;}
        .is-attacking-enemy{animation:atk-anim-enemy 0.3s ease;}
        .is-damaged{animation:dmg-anim 0.3s ease;}
        .is-healing{animation:heal-anim 0.5s ease;}
        .is-buffed{animation:buff-anim 0.5s ease;}
        .action-menu{display:flex;flex-direction:column;align-items:center;margin-top:15px;background:rgba(0,0,0,0.8);padding:15px;border-radius:8px;border:1px solid var(--accent-blue);}
        .action-buttons{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;}
        #battle-log{margin-top:15px;height:130px;overflow-y:auto;background:rgba(0,0,0,0.8);border:1px solid #444;padding:10px;font-family:monospace;font-size:13px;}
        .log-entry{margin-bottom:4px;color:#aaa;}
        .log-entry.player-atk{color:var(--accent-blue);}
        .log-entry.enemy-atk{color:var(--danger-red);}
        .log-entry.system{color:var(--primary-gold);}
        #action-order-bar{display:flex;gap:4px;align-items:center;padding:8px 10px;margin-bottom:12px;background:rgba(0,0,0,0.75);border-radius:6px;border:1px solid rgba(212,175,55,0.35);overflow-x:auto;min-height:58px;scrollbar-width:thin;}
        .aob-item{display:flex;flex-direction:column;align-items:center;gap:2px;flex-shrink:0;transition:transform 0.2s;}
        .aob-item img{width:36px;height:36px;border-radius:50%;border:2px solid #555;object-fit:cover;background:#111;}
        .aob-item.is-player img{border-color:var(--accent-blue);}
        .aob-item.is-enemy img{border-color:var(--danger-red);}
        .aob-item.current img{border-color:var(--primary-gold);box-shadow:0 0 10px var(--primary-gold);transform:scale(1.25);}
        .aob-item span{font-size:8px;color:#777;font-family:\'Orbitron\';white-space:nowrap;}
        .aob-arrow{color:#444;font-size:14px;flex-shrink:0;padding:0 1px;}
        #aob-label{font-size:9px;color:var(--primary-gold);font-family:\'Orbitron\';margin-right:6px;white-space:nowrap;}
        #attack-anim-layer{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:5000;}
        #anim-attacker{position:fixed;width:55px;height:55px;border-radius:50%;border:3px solid var(--accent-blue);object-fit:cover;display:none;box-shadow:0 0 25px var(--accent-blue),0 0 50px rgba(0,210,255,0.3);}
        .slash-burst-anim{position:fixed;pointer-events:none;z-index:5001;}
        .slash-burst-anim img{width:130px;height:130px;object-fit:contain;animation:slashBurstKf 0.5s ease-out forwards;transform-origin:center;}
        @keyframes slashBurstKf{0%{opacity:0;transform:translate(-50%,-50%) scale(0.2) rotate(-70deg);filter:brightness(4);}30%{opacity:1;transform:translate(-50%,-50%) scale(1.1) rotate(-45deg);}100%{opacity:0;transform:translate(-50%,-50%) scale(1.6) rotate(-25deg);}}
        .slash-trail{position:fixed;pointer-events:none;z-index:4999;height:2px;border-radius:2px;background:linear-gradient(90deg,transparent,var(--accent-blue),#fff,transparent);animation:trailFade 0.35s ease-out forwards;transform-origin:left center;}
        .slash-trail.enemy-trail{background:linear-gradient(90deg,transparent,var(--danger-red),#fff,transparent);}
        @keyframes trailFade{0%{opacity:0;}20%{opacity:1;}100%{opacity:0;}}
        .heal-burst-fx{position:absolute;inset:0;border-radius:6px;pointer-events:none;z-index:50;animation:healBurstKf 0.75s ease-out forwards;}
        @keyframes healBurstKf{0%{box-shadow:inset 0 0 0 rgba(76,175,80,0);background:rgba(76,175,80,0);}30%{box-shadow:inset 0 0 25px rgba(76,175,80,0.9),0 0 35px rgba(76,175,80,0.6);background:rgba(76,175,80,0.18);}100%{box-shadow:inset 0 0 0 rgba(76,175,80,0);background:rgba(76,175,80,0);}}
        .shield-burst-fx{position:absolute;inset:0;border-radius:6px;pointer-events:none;z-index:50;animation:shieldBurstKf 0.8s ease-out forwards;}
        @keyframes shieldBurstKf{0%{box-shadow:inset 0 0 0 rgba(135,206,250,0);background:rgba(135,206,250,0);}25%{box-shadow:inset 0 0 30px rgba(135,206,250,0.95),0 0 50px rgba(135,206,250,0.7);background:rgba(135,206,250,0.2);outline:2px solid var(--shield-white);}100%{box-shadow:inset 0 0 0 rgba(135,206,250,0);background:rgba(135,206,250,0);outline:2px solid transparent;}}
        .debuff-burst-fx{position:absolute;inset:0;border-radius:6px;pointer-events:none;z-index:50;animation:debuffBurstKf 0.85s ease-out forwards;}
        @keyframes debuffBurstKf{0%{box-shadow:inset 0 0 0 rgba(147,112,219,0);background:rgba(147,112,219,0);}20%{box-shadow:inset 0 0 35px rgba(147,112,219,1),0 0 50px rgba(147,112,219,0.8);background:rgba(147,112,219,0.3);}60%{box-shadow:inset 0 0 20px rgba(147,112,219,0.5);background:rgba(147,112,219,0.12);}100%{box-shadow:inset 0 0 0 rgba(147,112,219,0);background:rgba(147,112,219,0);}}
        .fx-particle{position:absolute;pointer-events:none;z-index:60;animation:fxParticleKf 1.1s ease-out forwards;font-size:13px;}
        @keyframes fxParticleKf{0%{opacity:1;transform:translateY(0) scale(1);}100%{opacity:0;transform:translateY(-65px) scale(0.4);}}
        .entity-card.has-debuff{animation:debuffPulse 2.5s ease-in-out infinite;}
        @keyframes debuffPulse{0%,100%{box-shadow:0 0 6px rgba(147,112,219,0.35);}50%{box-shadow:0 0 18px rgba(147,112,219,0.75),inset 0 0 12px rgba(147,112,219,0.25);}}
        .debuff-drip{position:absolute;top:4px;left:4px;display:flex;flex-direction:column;gap:2px;pointer-events:none;z-index:20;}
        .debuff-drip span{font-size:10px;animation:dripFloat 2s ease-in-out infinite;display:block;}
        .debuff-drip span:nth-child(2){animation-delay:0.6s;}
        .debuff-drip span:nth-child(3){animation-delay:1.2s;}
        @keyframes dripFloat{0%,100%{transform:translateY(0);opacity:0.5;}50%{transform:translateY(-5px);opacity:1;}}
        #main-menu-view{display:none;flex-direction:column;min-height:100vh;}
        #main-menu-view.active-view{display:flex;}
        .menu-hero{text-align:center;padding:40px 20px 20px;}
        .menu-hero h1{font-family:\'Orbitron\',sans-serif;font-size:2.4rem;background:linear-gradient(135deg,var(--primary-gold),var(--accent-blue),#ff6ec7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:none;letter-spacing:3px;}
        .menu-hero p{color:#aaa;margin-top:8px;font-size:14px;}
        .menu-hero .jade-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,215,0,0.12);border:1px solid rgba(255,215,0,0.3);border-radius:20px;padding:6px 18px;margin-top:12px;font-family:\'Orbitron\';font-size:15px;color:var(--primary-gold);}
        .mode-cards{display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:0 20px 30px;max-width:960px;margin:0 auto;width:100%;}
        @media(max-width:600px){.mode-cards{grid-template-columns:1fr;}}
        .mode-card{position:relative;border-radius:16px;padding:30px 24px;cursor:pointer;overflow:hidden;transition:transform 0.25s,box-shadow 0.25s;border:1px solid rgba(255,255,255,0.1);}
        .mode-card:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(0,0,0,0.5);}
        .mode-card.story{background:linear-gradient(135deg,rgba(0,130,180,0.25),rgba(0,60,100,0.6));border-color:rgba(0,210,255,0.3);}
        .mode-card.casual{background:linear-gradient(135deg,rgba(180,80,0,0.25),rgba(80,20,0,0.6));border-color:rgba(255,160,0,0.3);}
        .mode-card .mc-glow{position:absolute;top:-40px;right:-40px;width:180px;height:180px;border-radius:50%;opacity:0.12;}
        .mode-card.story .mc-glow{background:radial-gradient(circle,#00d2ff,transparent);}
        .mode-card.casual .mc-glow{background:radial-gradient(circle,#ffa500,transparent);}
        .mode-card .mc-icon{font-size:3rem;margin-bottom:14px;display:block;}
        .mode-card h2{font-family:\'Orbitron\';font-size:1.3rem;margin-bottom:8px;}
        .mode-card.story h2{color:var(--accent-blue);}
        .mode-card.casual h2{color:var(--primary-gold);}
        .mode-card p{color:#ccc;font-size:13px;line-height:1.6;margin-bottom:18px;}
        .mode-card .mc-btn{display:block;width:100%;padding:12px;border-radius:8px;font-family:\'Orbitron\';font-size:13px;font-weight:700;border:none;cursor:pointer;letter-spacing:1px;transition:filter 0.2s;}
        .mode-card .mc-btn:hover{filter:brightness(1.2);}
        .mode-card.story .mc-btn{background:linear-gradient(90deg,#0ea5e9,#2563eb);color:#fff;}
        .mode-card.casual .mc-btn{background:linear-gradient(90deg,#f59e0b,#ef4444);color:#fff;}
        #casual-view{display:none;flex-direction:column;min-height:100vh;}
        #casual-view.active-view{display:flex;}
        .casual-panel{max-width:680px;margin:0 auto;width:100%;padding:20px;}
        .stage-header{text-align:center;margin-bottom:24px;}
        .stage-number{font-family:\'Orbitron\';font-size:3.5rem;font-weight:900;line-height:1;}
        .stage-number.kroco{color:#4ade80;text-shadow:0 0 20px rgba(74,222,128,0.5);}
        .stage-number.miniboss{color:#fb923c;text-shadow:0 0 20px rgba(251,146,60,0.5);}
        .stage-number.boss{color:#f87171;text-shadow:0 0 25px rgba(248,113,113,0.7);}
        .stage-label{font-size:12px;color:#888;letter-spacing:3px;text-transform:uppercase;margin-bottom:4px;}
        .stage-type-badge{display:inline-block;padding:4px 16px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:2px;margin-top:8px;}
        .stage-type-badge.kroco{background:rgba(74,222,128,0.15);border:1px solid rgba(74,222,128,0.4);color:#4ade80;}
        .stage-type-badge.miniboss{background:rgba(251,146,60,0.15);border:1px solid rgba(251,146,60,0.4);color:#fb923c;}
        .stage-type-badge.boss{background:rgba(248,113,113,0.15);border:1px solid rgba(248,113,113,0.4);color:#f87171;animation:bossGlow 2s ease-in-out infinite;}
        @keyframes bossGlow{0%,100%{box-shadow:0 0 6px rgba(248,113,113,0.3);}50%{box-shadow:0 0 18px rgba(248,113,113,0.8);}}
        .stage-chunk-bar{display:flex;gap:4px;justify-content:center;margin:16px 0;}
        .stage-chunk-bar .scb-dot{width:22px;height:8px;border-radius:4px;transition:all 0.3s;}
        .stage-chunk-bar .scb-dot.done{background:var(--heal-green);}
        .stage-chunk-bar .scb-dot.current{background:var(--primary-gold);box-shadow:0 0 8px var(--primary-gold);}
        .stage-chunk-bar .scb-dot.miniboss-dot{background:rgba(251,146,60,0.4);}
        .stage-chunk-bar .scb-dot.boss-dot{background:rgba(248,113,113,0.4);}
        .stage-chunk-bar .scb-dot.pending{background:rgba(255,255,255,0.1);}
        .stage-info-cards{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;}
        .sic{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px;text-align:center;}
        .sic .sic-val{font-size:1.4rem;font-weight:700;font-family:\'Orbitron\';}
        .sic .sic-label{font-size:11px;color:#888;margin-top:4px;letter-spacing:1px;}
        .enemy-preview{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:16px;margin-bottom:20px;}
        .enemy-preview h4{font-size:12px;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;}
        .ep-list{display:flex;gap:10px;flex-wrap:wrap;}
        .ep-enemy{display:flex;flex-direction:column;align-items:center;gap:4px;}
        .ep-enemy img{width:52px;height:52px;border-radius:8px;object-fit:cover;border:2px solid rgba(255,255,255,0.1);}
        .ep-enemy.boss-preview img{border-color:var(--danger-red);box-shadow:0 0 10px rgba(248,113,113,0.4);}
        .ep-enemy span{font-size:9px;color:#aaa;text-align:center;max-width:60px;}
        .btn-casual-battle{width:100%;padding:18px;font-size:1.1rem;font-family:\'Orbitron\';letter-spacing:2px;border-radius:12px;border:none;cursor:pointer;font-weight:700;background:linear-gradient(90deg,#f59e0b,#ef4444,#f59e0b);background-size:200%;animation:gradShift 3s linear infinite;color:#fff;box-shadow:0 6px 30px rgba(239,68,68,0.4);transition:transform 0.2s;}
        .btn-casual-battle:hover{transform:scale(1.02);}
        @keyframes gradShift{0%{background-position:0%}100%{background-position:200%}}
        @media (max-width: 768px) {
            .char-grid{grid-template-columns:repeat(auto-fill,minmax(75px,1fr)); gap:6px;}
            .char-img{width:55px;height:55px;}
            .char-card-select{font-size:10px;padding:4px;}
            #action-order{left:2px;top:60px;width:35px;}
            .order-item img{width:28px;height:28px;}
            #battle-log{height:200px;font-size:10px;}
            .modal-content{width:95%;padding:15px;margin-top:20px;}
            .btn{padding:8px 12px;font-size:0.8rem;}
            .header-bar{flex-wrap:wrap;gap:8px;justify-content:center;}
            .page{padding:10px;}
            .battle-row{flex-direction:column;gap:15px;}
        }
    </style>
</head>
<body>\n
<!-- Daily Missions Modal -->
<div id="mission-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9999; justify-content:center; align-items:center;">
    <div class="glass-panel" style="width:400px; text-align:center;">
        <h2 style="color:var(--accent-blue); margin-bottom:15px;">&#x1F4DD; Misi Harian</h2>
        <div id="mission-list" style="display:flex; flex-direction:column; gap:10px; margin-bottom:20px;">
            <!-- Rendered via JS -->
        </div>
        <button class="hsr-btn" onclick="document.getElementById('mission-modal').style.display='none'">Tutup</button>
    </div>
</div>

<!-- Audio Elements -->
<audio id="bgm-menu" loop preload="auto"><source src="https://actions.google.com/sounds/v1/science_fiction/dark_space.ogg" type="audio/ogg"></audio>
<audio id="bgm-battle" loop preload="auto"><source src="https://actions.google.com/sounds/v1/science_fiction/epic_orchestral_space.ogg" type="audio/ogg"></audio>
<audio id="sfx-hit" preload="auto"><source src="https://actions.google.com/sounds/v1/impacts/crash.ogg" type="audio/ogg"></audio>
<audio id="sfx-ult" preload="auto"><source src="https://actions.google.com/sounds/v1/weapons/laser_gun_fire.ogg" type="audio/ogg"></audio>
<audio id="sfx-win" preload="auto"><source src="https://actions.google.com/sounds/v1/crowds/crowd_cheer.ogg" type="audio/ogg"></audio>
<audio id="bgm-battle" loop preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/01/18/audio_821db9a288.mp3" type="audio/mpeg"></audio>
<audio id="sfx-hit" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_1067d5ce39.mp3" type="audio/mpeg"></audio>
<audio id="sfx-ult" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/03/10/audio_c8c8a73467.mp3" type="audio/mpeg"></audio>
<audio id="sfx-win" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2021/08/04/audio_0625c1539c.mp3" type="audio/mpeg"></audio>

<div id="attack-anim-layer"><img id="anim-attacker" src="" alt=""></div>

<div id="login-view" class="spa-view active-view">
    <div class="glass-panel" style="margin:10vh auto;max-width:400px;text-align:center;">
        <h1 style="margin-bottom:20px;">&#x1F30C; HONKAI: WEB RAIL</h1>
        <button id="btn-user-login" class="hsr-btn blue" style="width:100%;">Mulai Game (Google)</button>
        <div style="margin:20px 0;border-top:1px solid rgba(255,255,255,0.1);position:relative;">
            <span style="position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:var(--panel-bg);padding:0 10px;font-size:12px;color:#888;">ADMIN</span>
        </div>
        <input type="email" id="admin-email" class="hsr-input" placeholder="Admin Email">
        <input type="password" id="admin-pass" class="hsr-input" placeholder="Password">
        <button id="btn-admin-login" class="hsr-btn" style="width:100%;">Login Server</button>
    </div>
</div>

<div id="main-menu-view" class="spa-view">
    <div class="menu-hero">
        <h1>&#x1F30C; HONKAI: WEB RAIL</h1>
        <p>Pilih mode permainan favoritmu</p>
        <div class="jade-badge" id="menu-jade-display">&#x1F48E; ...</div>
        <div style="margin-top:10px;">
            <button class="hsr-btn blue" onclick="openMissions()" style="margin-left:10px;">&#x1F4DD; Misi Harian</button>\n<button class="hsr-btn" onclick="signOut(auth)" style="padding:5px 14px;font-size:12px;">Logout</button>
        </div>
    </div>
    <div class="mode-cards">
        <div class="mode-card story" onclick="goStoryMode()">
            <div class="mc-glow"></div>
            <span class="mc-icon">&#x1F4D6;</span>
            <h2>STORY MODE</h2>
            <p>Ladeni 1 pertempuran klasik melawan grup musuh acak. Grind Stellar Jade cepat.</p>
            <div style="margin-bottom:10px;font-size:12px;color:#aaa;">&#x1F3C6; Menang: +600 &#x1F48E; &nbsp;|&nbsp; &#x1F480; Kalah: +100 &#x1F48E;</div>
            <button class="mc-btn">&#x25B6; MULAI STORY</button>
        </div>
        <div class="mode-card casual" onclick="goCasualMode()">
            <div class="mc-glow"></div>
            <span class="mc-icon">&#x2694;&#xFE0F;</span>
            <h2>CASUAL MODE</h2>
            <p>Petualangan bertahap dari Stage 1. Musuh makin kuat tiap 10 stage. Boss di stage 10, 20, 30...</p>
            <div style="margin-bottom:10px;font-size:12px;color:#aaa;">Stage: +50 &#x1F48E; &nbsp;|&nbsp; Mini-Boss: +150 &#x1F48E; &nbsp;|&nbsp; Boss: +300 &#x1F48E;</div>
            <button class="mc-btn">&#x2694; MULAI CASUAL</button>
        </div>
        <div class="mode-card su-mode" onclick="goSUMode()" style="background:rgba(80,20,80,0.8);border:1px solid #c026d3;">
            <div class="mc-glow" style="background: radial-gradient(circle at center, #c026d3 0%, transparent 60%);"></div>
            <span class="mc-icon" style="color:#c026d3;">✨</span>
            <h2>SIMULATED UNIVERSE</h2>
            <p>Lawan 5 stage berturut-turut dengan buff acak. Energy & HP terbawa ke stage berikutnya.</p>
            <div style="margin-bottom:10px;font-size:12px;color:#aaa;">Menang 5 Stage: +5000 &#x1F48E;</div>
            <button class="mc-btn" style="background:#c026d3;color:#fff;">▶ MULAI SU</button>
        </div>
    </div>
</div>
<div style="max-width:800px;margin:30px auto;background:rgba(0,0,0,0.6);border:2px solid #333;border-radius:12px;padding:20px;box-shadow:0 0 20px rgba(59,130,246,0.2);">
    <h3 style="text-align:center;color:var(--accent-blue);font-family:'Orbitron';text-shadow:0 0 10px rgba(59,130,246,0.5);margin-bottom:15px;">&#x1F3C6; TOP 10 CASUAL PLAYERS &#x1F3C6;</h3>
    <div id="leaderboard-list" style="display:flex;flex-direction:column;gap:10px;">
        <div style="text-align:center;color:#888;">Memuat Leaderboard...</div>
    </div>
</div>
</div>

<div id="su-buff-view" class="spa-view">
    <div class="casual-panel glass-panel" style="text-align:center; max-width:600px; margin: 10vh auto;">
        <h2 style="color:#c026d3; margin-bottom:10px;">✨ Simulated Universe</h2>
        <p style="margin-bottom:20px;">Kamu memenangkan Stage <span id="su-stage-label"></span>. Pilih 1 Buff untuk sisa perjalanan!</p>
        <div id="su-buff-options" style="display:flex; flex-direction:column; gap:10px;"></div>
    </div>
</div>

<div id="casual-view" class="spa-view">
    <div class="navbar">
        <h2>&#x2694;&#xFE0F; Casual Mode</h2>
        <button class="hsr-btn" onclick="navigateTo(\'main-menu-view\')" style="padding:5px 10px;">&#x2190; Menu</button>
    </div>
    <div class="casual-panel glass-panel">
        <div class="stage-header">
            <div class="stage-label">STAGE</div>
            <div class="stage-number" id="casual-stage-num">1</div>
            <div id="casual-stage-badge" class="stage-type-badge kroco">KROCO FIGHT</div>
        </div>
        <div class="stage-chunk-bar" id="casual-chunk-bar"></div>
        <div class="stage-info-cards">
            <div class="sic"><div class="sic-val" id="casual-reward-val" style="color:var(--primary-gold);">50 &#x1F48E;</div><div class="sic-label">REWARD MENANG</div></div>
            <div class="sic"><div class="sic-val" id="casual-scale-val">1.0x</div><div class="sic-label">LEVEL MUSUH</div></div>
        </div>
        <div class="enemy-preview"><h4>&#x1F50D; Pratinjau Musuh</h4><div class="ep-list" id="casual-enemy-preview"></div></div>
        <button class="btn-casual-battle" onclick="startCasualBattle()">&#x2694;&#xFE0F; MULAI STAGE</button>
        <button class="hsr-btn" style="width:100%;margin-top:10px;" onclick="navigateTo(\'select-view\')">&#x1F3AD; Ganti Party Dulu</button>
    </div>
</div>

<div id="select-view" class="spa-view">
    <div class="navbar">
        <h2>Pilih 4 Anggota Party</h2>
        <div style="display:flex;gap:10px;align-items:center;">
            <button class="hsr-btn" onclick="navigateTo(\'main-menu-view\')" style="padding:5px 10px;">&#x2190; Menu</button>
            <button class="hsr-btn blue" onclick="suggestTeam()">Saran Tim</button>
            <button class="hsr-btn" onclick="openPathInfo()">Info Path</button>
            <h3 id="jade-display" style="color:var(--jade-pink);text-shadow:0 0 5px var(--jade-pink);margin:0 10px;">&#x1F48E; Loading...</h3>
            <button class="hsr-btn blue" onclick="openMissions()" style="margin-left:10px;">&#x1F4DD; Misi Harian</button>\n<button class="hsr-btn" onclick="signOut(auth)" style="padding:5px 10px;">Logout</button>
        </div>
    </div>
    <div class="glass-panel">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <p>Klik karakter untuk Detail, Beli, &amp; Upgrade Eidolon.</p>
            <h3 id="party-counter">Terpilih: 0/4</h3>
        </div>
        <div id="char-roster" class="char-grid"></div>
        <button id="btn-start-battle" class="hsr-btn blue" style="width:100%;margin-top:20px;font-size:18px;" disabled onclick="startBattle()">MULAI PERTEMPURAN</button>
    </div>
</div>

<div id="char-modal" class="modal-overlay">
    <div class="modal-content" id="modal-content-area"></div>
</div>

<div id="user-view" class="spa-view">
    <div class="navbar">
        <h2 id="battle-title">Medan Pertempuran</h2>
        <button class="hsr-btn" onclick="fleeBattle()" style="padding:5px 10px;">Flee</button>
    </div>
    <div class="glass-panel">
        
    <div style="display:flex; gap:10px; margin-bottom:10px; justify-content:flex-end; width:100%;">
        <button id="btn-speed" class="hsr-btn" onclick="toggleSpeed()" style="padding:5px 10px; font-size:12px;">&#x23E9; 1x</button>
        <button id="btn-auto" class="hsr-btn" onclick="toggleAuto()" style="padding:5px 10px; font-size:12px;">&#x1F916; Auto: OFF</button>
    </div>
\n        <div id="action-order-bar"><span id="aob-label">ORDER</span></div>
        <div class="battle-wrapper">
            <div class="team-container" id="player-ui"></div>
            <div class="team-container enemy-container" id="enemy-ui"></div>
        </div>
        <div class="action-menu" id="action-menu">
            <div style="width:100%;text-align:center;margin-bottom:10px;">
                <h3 id="active-char-name">Giliran: -</h3>
                <p id="active-char-desc" style="font-size:12px;color:#aaa;">Mechanic: -</p>
            </div>
            <div class="sp-wrapper" id="sp-display"></div>
            <div class="action-buttons">
                <button class="hsr-btn" onclick="playerAction(\'basic\')">Basic Attack (+1 SP)</button>
                <button id="btn-skill" class="hsr-btn blue" onclick="playerAction(\'skill\')">Skill (-1 SP)</button>
                <button id="btn-ult" class="hsr-btn ult" onclick="playerAction(\'ultimate\')">Ultimate (MAX)</button>
            </div>
        </div>
        
        <div id="su-resonance-container" style="display:none; text-align:center; margin-bottom:10px;">
            <button id="btn-resonance" class="hsr-btn" style="background:var(--accent-orange); width:100%; font-weight:bold; color:#000; box-shadow:0 0 10px var(--accent-orange);" onclick="useResonance()">&#x26A1; PATH RESONANCE (0%)</button>
        </div>
\n        <div id="battle-log"></div>
    </div>
</div>

<div id="admin-view" class="spa-view">
    <div class="navbar"><h2>Admin Server</h2><button class="hsr-btn blue" onclick="openMissions()" style="margin-left:10px;">&#x1F4DD; Misi Harian</button>\n<button class="hsr-btn" onclick="signOut(auth)">Logout</button></div>
    <div class="glass-panel" style="max-width:500px;margin:0 auto;">
        <h3>Stat Boss Global</h3>
        <input type="text" id="set-boss-name" class="hsr-input" value="Doomsday Beast" style="margin-top:15px;">
        <input type="number" id="set-boss-hp" class="hsr-input" placeholder="Boss Max HP" value="5000">
        <input type="number" id="set-boss-dmg" class="hsr-input" placeholder="Boss Base DMG" value="250">
        <button id="btn-save-settings" class="hsr-btn blue" style="width:100%;">Update Data</button>
    </div>
</div>
'''

JS_PART1 = '''
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup, signInWithEmailAndPassword, onAuthStateChanged, signOut as firebaseSignOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, collection, query, orderBy, limit, getDocs } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";
const firebaseConfig = { apiKey:"AIzaSyD6-yTDQSjPyBvfCqgwKTdJPlRLkFj-MWE", authDomain:"myhonkairail-a1e1d.firebaseapp.com", projectId:"myhonkairail-a1e1d", storageBucket:"myhonkairail-a1e1d.firebasestorage.app", messagingSenderId:"122125592488", appId:"1:122125592488:web:dbad579ea52304d6339f9d" };
const app = initializeApp(firebaseConfig); window.auth = getAuth(app); const db = getFirestore(app);

const pathInfo = {
    'Destruction':'Menyerang dan bertahan seimbang. Unggul dalam solo & area.',
    'Hunt':'Spesialis serangan Target Tunggal (Single Target) mematikan.',
    'Erudition':'Spesialis serangan Area (AoE) untuk menyapu banyak musuh.',
    'Harmony':'Spesialis Support. Memberikan Buff untuk memperkuat party.',
    'Nihility':'Spesialis Debuff. Mengurangi pertahanan musuh & memicu DoT.',
    'Preservation':'Spesialis Bertahan. Melindungi party dengan Shield tebal.',
    'Abundance':'Spesialis Penyembuhan. Memulihkan HP party (Healer).',
    'Remembrance':'Spesialis Memory. Memanggil Mem untuk support & serangan.'
};

// ===== AZRIEL / MC MULTI-PATH SYSTEM =====
// Azriel IS the Trailblazer. One character, 4 paths, separate eidolons per path.
const mcPaths = {
    physical:    { pathKey:'physical',    subname:'Destruction', role:'Destruction',  hp:1800, atk:320, spd:100, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8001.png', color:'#c084fc', element:'Physical', desc:'Path of Destruction. Skill: 130% ATK AoE Blade. Ulti: 300% Heavy Slash semua musuh \\u26d4', eEffects:['E1: Blade DMG +25% & Bleed 30%','E2: Ulti tembus 15% DEF & regen 2 SP saat kill','E3: Skill Lvl +2, Talent +2','E4: Kebal Debuff saat HP<50%, DMG +20%','E5: Ult Lvl +2','E6: Kill di Ulti trigger ledakan 200% ATK AoE!'] },
    fire:        { pathKey:'fire',        subname:'Preservation', role:'Preservation', hp:2200, atk:180, spd:100, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8003.png', color:'#fb923c', element:'Fire',     desc:'Path of Preservation. Skill: Shield 1400 HP + Taunt. Ulti: Party Shield & Cleanse \\ud83d\\udee1', eEffects:['E1: Shield +30% & Fire Counter saat diserang','E2: Ulti beri Fire RES +25% & ATK +20%','E3: Skill Lvl +2, Talent +2','E4: Counter melemahkan musuh -15% DEF','E5: Ult Lvl +2','E6: Shield meledak saat habis, 250% ATK ke semua musuh!'] },
    imaginary:   { pathKey:'imaginary',   subname:'Harmony',     role:'Harmony',      hp:1850, atk:220, spd:101, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8005.png', color:'#facc15', element:'Imaginary',desc:'Path of Harmony. Skill: Super Break DMG tim +50% (2 turn). Ulti: AoE Imaginary + Regen Toughness \\u2b50', eEffects:['E1: Super Break DMG +20% extra, durasi +1','E2: Ally full toughness: Super Break +30%','E3: Skill Lvl +2, Talent +2','E4: Break Effect tim +15%','E5: Ult Lvl +2','E6: Super Break menembus SEMUA RES musuh!'] },
    remembrance: { pathKey:'remembrance', subname:'Remembrance', role:'Remembrance',  hp:1900, atk:230, spd:100, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8007.png', color:'#67e8f9', element:'Ice',      desc:'Path of Remembrance. Skill: Summon Mem. Ulti: Mem Mode, Ice AoE + Buff \\u2744', eEffects:['E1: Mem ATK +30% & CRIT Rate +15%','E2: Saat Mem serang, tim regen 1 SP','E3: Skill Lvl +2, Talent +2','E4: Memory DMG +25% saat Mem Mode aktif','E5: Ult Lvl +2','E6: Mem dapat giliran ekstra & Ice DMG menembus RES!'] }
};

let activeMcPath = localStorage.getItem('mcPath') || 'imaginary';
function getMcEidolonKey() { return 'mc_' + activeMcPath; }
function getMcData() {
    let p = mcPaths[activeMcPath];
    return { id:'mc', name:'Azriel', price:0, isMc:true, ...p };
}
window.setMcPath = function(p) {
    activeMcPath = p;
    localStorage.setItem('mcPath', p);
    let idx = charDB.findIndex(x => x.id === 'mc');
    if (idx !== -1) Object.assign(charDB[idx], getMcData());
    let pi = state && state.party ? state.party.findIndex(x => x.id === 'mc') : -1;
    if (pi !== -1) {
        let mc = getMcData();
        let eLvl = state.eidolons[getMcEidolonKey()] || 0;
        let bonusMulti = 1 + eLvl * 0.10;
        let prev = state.party[pi];
        state.party[pi] = { ...mc, eLvl, maxHp:Math.floor(mc.hp*bonusMulti), hp:Math.min(prev.hp||mc.hp, Math.floor(mc.hp*bonusMulti)), atk:Math.floor(mc.atk*bonusMulti), spd:mc.spd, shield:prev.shield||0, buffAtk:prev.buffAtk||0, resPen:prev.resPen||0, energy:prev.energy||0, maxEnergy:100, statuses:prev.statuses||[] };
    }
    renderCharSelect();
    openCharModal('mc');
};

const starters = ['mc','danheng','march7','natasha'];
const charDB = [
    { ...getMcData() },
    { id:'danheng', name:'Dan Heng', role:'Hunt', hp:1200, atk:220, spd:110, price:0, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1002.png', desc:'Skill: 200% ATK. Ulti: 400% ATK Nuke DMG', eEffects:['E1: ATK +10%','E2: CRIT DMG +15%','E3: Skill Lvl +2','E4: Pasif trigger 2x','E5: Ult Lvl +2','E6: Ultimate menembus 20% Wind RES'] },
    { id:'march7', name:'March 7th', role:'Preservation', hp:2000, atk:130, spd:101, price:0, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1001.png', desc:'Skill: Shield 1000 HP. Pasif: Auto Counter-attack', eEffects:['E1: Shield +15%','E2: Shield beri regen HP','E3: Skill Lvl +2','E4: 2 Counter per turn','E5: Ult Lvl +2','E6: Counter sembuhkan HP tim'] },
    { id:'natasha', name:'Natasha', role:'Abundance', hp:2000, atk:130, spd:98, price:0, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1105.png', desc:'Skill: Heal 1200 HP. Ulti: Heal 2000 HP All', eEffects:['E1: Heal HP rendah +20%','E2: Ultimate aktif otomatis jika teman sekarat','E3: Skill Lvl +2','E4: Energy regen +15%','E5: Ult Lvl +2','E6: Heal 2x lipat!'] },
    { id:'seele', name:'Seele', role:'Hunt', hp:1200, atk:220, spd:115, price:800, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1102.png', desc:'Ulti: 450% ATK. Pasif: Kill = Extra Turn', eEffects:['E1: CRIT Rate +15% ke musuh sekarat','E2: SPD Buff bisa ditumpuk','E3: Skill Lvl +2','E4: 15 Energy saat kill','E5: Ult Lvl +2','E6: Ultimate beri ledakan beruntun!'] },
    { id:'himeko', name:'Himeko', role:'Erudition', hp:1200, atk:220, spd:94, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1003.png', desc:'Skill: 120% ATK AoE. Ulti: 250% ATK AoE Fire', eEffects:['E1: Tambah SPD setelah follow-up','E2: DMG ke HP<50% +15%','E3: Skill Lvl +2','E4: Charge lebih cepat','E5: Ult Lvl +2','E6: Ultimate serang 2x'] },
    { id:'gepard', name:'Gepard', role:'Preservation', hp:2100, atk:170, spd:92, price:1200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1104.png', desc:'Ulti: Shield 1800 HP ke semua Party', eEffects:['E1: Taunt rate naik','E2: Beku bikin musuh slow 20%','E3: Skill Lvl +2','E4: Effect RES tim +20%','E5: Ult Lvl +2','E6: Revive Gepard 100% HP'] },
    { id:'bronya', name:'Bronya', role:'Harmony', hp:1500, atk:220, spd:112, price:1200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1101.png', desc:'Ulti: Buff 60% ATK ke semua Party', eEffects:['E1: 50% peluang kembalikan 1 SP saat Skill','E2: Target skill SPD +30%','E3: Skill Lvl +2','E4: Bronze menyusul saat rekan break','E5: Ult Lvl +2','E6: Durasi buff +1 giliran'] },
    { id:'tingyun', name:'Tingyun', role:'Harmony', hp:1400, atk:180, spd:112, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1202.png', desc:'Skill: Buff 80% ATK ke DPS', eEffects:['E1: DPS dapat bonus SPD','E2: DPS kill dapat energy extra','E3: Skill Lvl +2','E4: ATK buff naik 20%','E5: Ult Lvl +2','E6: Ultimate beri 60 Energy ke target'] },
    { id:'kafka', name:'Kafka', role:'Nihility', hp:1500, atk:220, spd:115, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1005.png', desc:'Skill: 150% ATK + DoT Shock. Ulti: 200% ATK AoE + Shock', eEffects:['E1: DoT tim +30%','E2: DoT ally +25% DMG','E3: Skill Lvl +2','E4: Energy regen saat Shock meledak','E5: Ult Lvl +2','E6: Shock multiplier naik 156%'] },
    { id:'blade', name:'Blade', role:'Destruction', hp:1300, atk:260, spd:97, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1205.png', desc:'Ulti: Kuras 800 HP diri, deal 350% ATK AoE', eEffects:['E1: Ulti makin sakit sesuai HP hilang','E2: CRIT Rate +15% saat buff aktif','E3: Skill Lvl +2','E4: Max HP naik saat kena serang','E5: Ult Lvl +2','E6: Charge Follow-up lebih cepat 1 stack'] },
    { id:'jingyuan', name:'Jing Yuan', role:'Erudition', hp:1300, atk:260, spd:103, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1204.png', desc:'Ulti: 250% ATK AoE, panggil Lightning Lord', eEffects:['E1: LL serang menyebar ekstra 25%','E2: Setelah LL serang, tim DMG +20%','E3: Skill Lvl +2','E4: LL kasi energy','E5: Ult Lvl +2','E6: LL tembus DEF 20% tiap hit'] },
    { id:'bailu', name:'Bailu', role:'Abundance', hp:2100, atk:170, spd:98, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1211.png', desc:'Pasif: Heal saat tim dipukul. Ulti: Heal 2000 HP', eEffects:['E1: Energy penuh jika Invigoration di max HP','E2: Ulti beri +15% Heal Max','E3: Skill Lvl +2','E4: Tiap heal skill +10% DMG buff','E5: Ult Lvl +2','E6: Bisa Revive 2 kali!'] },
    { id:'silverwolf', name:'Silver Wolf', role:'Nihility', hp:1500, atk:220, spd:107, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1006.png', desc:'Skill: DEF Shred -40%. Ulti: 350% ATK Nuke', eEffects:['E1: Energy pulih dari debuff','E2: Semua musuh RES -20%','E3: Skill Lvl +2','E4: Extra DMG dari Ulti per debuff','E5: Ult Lvl +2','E6: DMG Nuke +100% jika banyak debuff'] },
    { id:'luocha', name:'Luocha', role:'Abundance', hp:2100, atk:170, spd:100, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1203.png', desc:'Ulti: 150% ATK AoE + Auto Heal Tim', eEffects:['E1: Field aktif = Tim ATK +20%','E2: Heal HP rendah makin kencang, HP penuh jadi Shield','E3: Skill Lvl +2','E4: Field melemahkan musuh -12%','E5: Ult Lvl +2','E6: Ulti urai RES musuh 20%'] },
    { id:'acheron', name:'Acheron', role:'Nihility', hp:1800, atk:300, spd:101, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1308.png', desc:'Ulti: 450% ATK abaikan DEF musuh', eEffects:['E1: CRIT Rate +18% ke debuff','E2: Hanya butuh 1 Nihility di tim untuk full pasif','E3: Skill Lvl +2','E4: Musuh kena rentan Ulti','E5: Ult Lvl +2','E6: DMG Ult pecah tembus 20% RES'] },
    { id:'jingliu', name:'Jingliu', role:'Destruction', hp:1400, atk:300, spd:103, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1212.png', desc:'Ulti: 350% ATK Massive Ice DMG Blast', eEffects:['E1: CRIT DMG +24%','E2: DMG Ult naik pasca skill','E3: Skill Lvl +2','E4: Sedot HP tim +10% ATK cap','E5: Ult Lvl +2','E6: Stack Syzygy cap +1, DMG +50%'] },
    { id:'sparkle', name:'Sparkle', role:'Harmony', hp:1800, atk:300, spd:108, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1306.png', desc:'Ulti: Memulihkan Max SP ke seluruh Party!', eEffects:['E1: Buff durasi +1 & ATK +40%','E2: Ignore 8% DEF per stack','E3: Skill Lvl +2','E4: Max SP jadi 8','E5: Ult Lvl +2','E6: Buff CRIT DMG nembus ke seluruh tim'] },
    { id:'aventurine', name:'Aventurine', role:'Preservation', hp:2200, atk:210, spd:100, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1304.png', desc:'Skill: Shield 800 HP AoE. Ulti: Nuke & Debuff', eEffects:['E1: Ulti memicu Shield & Tim CRIT DMG +20%','E2: Basic Atk turunkan RES musuh 12%','E3: Skill Lvl +2','E4: Shield naik, FUA 3x mematikan','E5: Ult Lvl +2','E6: DMG +50% per anggota ber-Shield'] },
    { id:'fuxuan', name:'Fu Xuan', role:'Preservation', hp:2200, atk:210, spd:100, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1208.png', desc:'Pasif: Mitigasi DMG. Ulti: Heal & AoE DMG', eEffects:['E1: Matrix beri +30% CRIT DMG','E2: Rekan mati auto Revive 1x','E3: Skill Lvl +2','E4: Energy Regen kalau rekan diserang','E5: Ult Lvl +2','E6: DMG Ult dari total HP yang diserap'] },
    { id:'ruanmei', name:'Ruan Mei', role:'Harmony', hp:2200, atk:380, spd:107, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1303.png', desc:'S-TIER: Res PEN, DEF Shred, ATK Buff 150% All Party', eEffects:['E1: Durasi Buff +1 turn','E2: ATK +40% ke musuh kena Break','E3: Skill Lvl +2','E4: Break Effect +20%','E5: Ult Lvl +2','E6: RES PEN menembus 200%!'] },
    { id:'firefly', name:'Firefly', role:'Destruction', hp:1600, atk:340, spd:104, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1310.png', desc:'Ulti: Mode SAM, 400% ATK Super Break DMG', eEffects:['E1: Skill saat SAM tidak pakai SP','E2: Giliran ekstra saat musuh Break/Kill','E3: Skill Lvl +2','E4: Effect RES +50% saat SAM','E5: Ult Lvl +2','E6: Break nembus DEF 20%!'] },
    { id:'blackswan', name:'Black Swan', role:'Nihility', hp:1800, atk:300, spd:101, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1307.png', desc:'Skill: 180% ATK + Stack Arcana DoT', eEffects:['E1: Musuh turun 25% Element RES sesuai DoT','E2: Arcana menyebar ke musuh sebelah','E3: Skill Lvl +2','E4: Musuh Effect RES -10%','E5: Ult Lvl +2','E6: 65% peluang trigger Arcana tiap hit'] },
    { id:'robin', name:'Robin', role:'Harmony', hp:1800, atk:300, spd:112, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1309.png', desc:'Ulti: Party Action Advance + 100% ATK Buff', eEffects:['E1: Tim dapat 24% RES PEN All Element','E2: Tim SPD naik 16%','E3: Skill Lvl +2','E4: Immune CC saat bernyanyi','E5: Ult Lvl +2','E6: Serangan Robin +200% CRIT DMG!'] },
    { id:'ratio', name:'Dr. Ratio', role:'Hunt', hp:1400, atk:300, spd:103, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1305.png', desc:'Skill: 200% ATK. Pasif: Follow-up Attack (Chalk)', eEffects:['E1: Max Stack Buff +4','E2: Follow-up DMG dari debuff musuh','E3: Skill Lvl +2','E4: Pulih 15 Energy saat kapur','E5: Ult Lvl +2','E6: Ult nambah kapur 1x & DMG +50%'] },
    { id:'huohuo', name:'Huohuo', role:'Abundance', hp:2400, atk:250, spd:101, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1217.png', desc:'Skill: Heal Blast. Ulti: Buff ATK & Energy Party', eEffects:['E1: SPD Tim +12% selagi buff aktif','E2: Bisa hidupkan 2 teman mati otomatis','E3: Skill Lvl +2','E4: Heal makin deras ke target sekarat','E5: Ult Lvl +2','E6: Tiap di-heal tim +50% DMG Buff!'] },
    { id:'feixiao', name:'Feixiao', role:'Hunt', hp:2000, atk:420, spd:112, price:3500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1220.png', desc:'Ulti: 480% ATK Sky-Piercing Nuke. FUA tiap rekan serang', eEffects:['E1: FUA DMG +20% & charge lebih cepat','E2: CRIT DMG +36% ke musuh debuff','E3: Skill Lvl +2','E4: Ult mereduksi 30% Toughness Bar','E5: Ult Lvl +2','E6: Ult DMG +50% & auto counter saat rekan kena serang!'] },
    { id:'boothill', name:'Boothill', role:'Hunt', hp:2000, atk:420, spd:107, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1315.png', desc:'Skill: Branded + Fire Break. Ulti: 420% ATK + Extra Break', eEffects:['E1: Branded duration +1 & Break DMG +25%','E2: Break Effect +30%, tembus 20% Fire RES','E3: Skill Lvl +2','E4: Regen 20 energy saat musuh Break','E5: Ult Lvl +2','E6: Ulti trigger extra Break + 100% Fire DMG!'] },
    { id:'yunli', name:'Yunli', role:'Destruction', hp:2000, atk:420, spd:100, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1221.png', desc:'Skill: 180% ATK. Counter: 320% ATK saat diserang', eEffects:['E1: Counter rate +35% & DMG +20%','E2: Saat counter, tim ATK +20%','E3: Skill Lvl +2','E4: Counter tembus 15% DEF','E5: Ult Lvl +2','E6: Counter jadi AoE & CRIT DMG +120%!'] },
    { id:'jiaoqiu', name:'Jiaoqiu', role:'Nihility', hp:2200, atk:380, spd:98, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1218.png', desc:'Skill: Ashen Roast -40% RES. Ulti: Hellscape Field', eEffects:['E1: Hellscape +25% Ulti DMG','E2: Ashen Roast stack +2 di awal battle','E3: Skill Lvl +2','E4: Tim +15% DMG saat Hellscape aktif','E5: Ult Lvl +2','E6: Hellscape memicu ledakan saat musuh dihantam'] },
    { id:'sunday', name:'Sunday', role:'Harmony', hp:2200, atk:380, spd:107, price:3500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1313.png', desc:'Ulti: Action advance DPS + CRIT DMG Buff massive', eEffects:['E1: CRIT DMG buff +20% extra','E2: Regen 1 SP per turn otomatis','E3: Skill Lvl +2','E4: Target DPS immune CC saat buff aktif','E5: Ult Lvl +2','E6: DMG DPS +80% selama buff Sunday aktif!'] },
    { id:'fugue', name:'Fugue', role:'Nihility', hp:2200, atk:380, spd:107, price:3500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1225.png', desc:'Skill: Toughness Shred +50%. Super Break amp.', eEffects:['E1: Super Break DMG +15% tim','E2: Toughness Reduction +30%','E3: Skill Lvl +2','E4: Break tim +20% BE','E5: Ult Lvl +2','E6: Super Break jadi AoE ke semua musuh!'] },
    { id:'rappa', name:'Rappa', role:'Erudition', hp:2000, atk:420, spd:96, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1317.png', desc:'Skill: AoE Toughness Shred. Ulti: Ninjutsu Mode Super Break', eEffects:['E1: Ninjutsu duration +1 turn','E2: Regen extra Charge saat musuh Break','E3: Skill Lvl +2','E4: Super Break DMG +25% di Ninjutsu mode','E5: Ult Lvl +2','E6: Ninjutsu Blast DMG +80%!'] },
    { id:'gallagher', name:'Gallagher', role:'Abundance', hp:2200, atk:210, spd:98, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1301.png', desc:'Skill: Heal + Besotted debuff. Ulti: AoE + Heal Burst', eEffects:['E1: Besotted musuh kena +20% Break DMG','E2: Regen 1 SP saat ally di-heal','E3: Skill Lvl +2','E4: Healer efektif +15%','E5: Ult Lvl +2','E6: Ulti heal otomatis tiap turn + Cleanse!'] },
    { id:'lingsha', name:'Lingsha', role:'Abundance', hp:2800, atk:330, spd:103, price:3500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1222.png', desc:'Skill: Heal AoE + Fuyuan summon. Ulti: Cleanse + Super Break buff', eEffects:['E1: Fuyuan attack +30% DMG','E2: Super Break ally +20%','E3: Skill Lvl +2','E4: Heal saat musuh Break','E5: Ult Lvl +2','E6: Fuyuan jadi massive AoE!'] },
    { id:'moze', name:'Moze', role:'Hunt', hp:1600, atk:340, spd:105, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1223.png', desc:'Skill: Mark musuh. Pasif: FUA Charge saat rekan serang', eEffects:['E1: FUA DMG +25%','E2: Mark musuh kena +15% DMG dari semua','E3: Skill Lvl +2','E4: Charge FUA lebih cepat','E5: Ult Lvl +2','E6: FUA jadi 2x serangan beruntun!'] },
    { id:'dhil', name:'Imbibitor Lunae', role:'Destruction', hp:2000, atk:420, spd:102, price:3500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1213.png', desc:'Skill: Enhance Basic ATK. Ulti: Massive AoE Imaginary', eEffects:['E1: Extra stack','E2: 100% Action Advance after Ulti','E3: Skill Lvl +2','E4: Buff durasi +1','E5: Ult Lvl +2','E6: Penetrasi RES 60%'] },
    { id:'herta', name:'Herta', role:'Erudition', hp:1200, atk:220, spd:100, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1013.png', desc:'Pasif: Kuru-kuru saat musuh <50% HP', eEffects:['E1: Basic ATK nambah DMG','E2: Kuru-kuru nambah CRIT Rate','E3: Skill Lvl +2','E4: Kuru-kuru DMG +10%','E5: Ult Lvl +2','E6: Ultimate nambah ATK'] },
    { id:'pela', name:'Pela', role:'Nihility', hp:1500, atk:220, spd:105, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1106.png', desc:'Ulti: Kurangi DEF seluruh musuh (AoE)', eEffects:['E1: Regen Energy saat bunuh musuh','E2: SPD naik setelah hapus buff','E3: Skill Lvl +2','E4: Skill kurangi Ice RES','E5: Ult Lvl +2','E6: Extra DMG ke musuh kena debuff'] },
    { id:'lynx', name:'Lynx', role:'Abundance', hp:2100, atk:170, spd:100, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1110.png', desc:'Ulti: Heal AoE + Cleanse Debuff', eEffects:['E1: Heal naik untuk HP rendah','E2: Cegah 1 Debuff','E3: Skill Lvl +2','E4: Nambah ATK dari Max HP Lynx','E5: Ult Lvl +2','E6: Nambah Max HP dan Effect RES'] },
    { id:'topaz', name:'Topaz & Numby', role:'Hunt', hp:2000, atk:420, spd:104, price:3200, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1112.png', desc:'Skill: Mark musuh. Numby akan FUA ke target Mark', eEffects:['E1: Numby DMG +20%','E2: Pulih Energy','E3: Skill Lvl +2','E4: Action Advance','E5: Ult Lvl +2','E6: Numby serang 2x lipat!'] },
    { id:'jade', name:'Jade', role:'Erudition', hp:1600, atk:340, spd:103, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1314.png', desc:'Skill: Kontrak dengan sekutu. Ulti: AoE Quantum DMG', eEffects:['E1: FUA DMG +20%','E2: CRIT Rate +15%','E3: Skill Lvl +2','E4: Penetrasi DEF','E5: Ult Lvl +2','E6: Quantum PEN +20%'] },
    { id:'aglaea', name:'Aglaea', role:'Remembrance', hp:2200, atk:380, spd:106, price:3500, img:'https://ui-avatars.com/api/?name=Aglaea&background=a855f7&color=fff', desc:'Summon: Garmentmaker. Serangan mematikan dan utility', eEffects:['E1: Garmentmaker +25% DMG','E2: Action Advance Garmentmaker','E3: Skill Lvl +2','E4: Penetrasi RES','E5: Ult Lvl +2','E6: DMG 2x lipat'] },
    { id:'welt', name:'Welt', role:'Nihility', hp:1600, atk:260, spd:102, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1004.png', desc:'Skill: Kurangi SPD musuh. Ulti: AoE Imprison & Slow', eEffects:['E1: Extra DMG setelah Ulti','E2: Regen Energy per musuh kena slow','E3: Skill Lvl +2','E4: Skill punya +10% base chance slow','E5: Ult Lvl +2','E6: Skill mantul ke musuh ekstra!'] },
    { id:'clara', name:'Clara', role:'Destruction', hp:1400, atk:300, spd:90, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1107.png', desc:'Svarog Counter! Tiap dipukul, Svarog bales.', eEffects:['E1: Mark tidak hilang saat skill','E2: Ulti beri ATK +30%','E3: Skill Lvl +2','E4: Kena hit, kurangin DMG 30%','E5: Ult Lvl +2','E6: Svarog punya 50% chance counter hit ke teman!'] },
    { id:'yanqing', name:'Yanqing', role:'Hunt', hp:1400, atk:300, spd:109, price:2000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1209.png', desc:'Soulsteel Sync: CRIT Rate tinggi. Hilang jika kena hit.', eEffects:['E1: DMG ke musuh beku +60%','E2: Regen Energy saat Sync aktif','E3: Skill Lvl +2','E4: Sync tembus 12% RES','E5: Ult Lvl +2','E6: Durasi buff Ulti tambah 1 turn!'] },
    { id:'argenti', name:'Argenti', role:'Erudition', hp:1600, atk:340, spd:103, price:2500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1302.png', desc:'Ulti 90 vs 180 Energy. AoE Physical nuker!', eEffects:['E1: Max Apotheosis buff + CRIT DMG','E2: Ulti 180 Energy deal +40% DMG jika musuh banyak','E3: Skill Lvl +2','E4: Mulai battle langsung 2 stack','E5: Ult Lvl +2','E6: Ulti 180 Energy abaikan 30% DEF!'] },
    { id:'asta', name:'Asta', role:'Harmony', hp:1400, atk:180, spd:106, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1009.png', desc:'Skill: Fire Break tinggi. Ulti: SPD seluruh tim meroket!', eEffects:['E1: Skill nambah 1 hit extra','E2: Stack gak ngurang pas pake Ulti','E3: Skill Lvl +2','E4: Energy Regen +15% saat stack tinggi','E5: Ult Lvl +2','E6: Stack ngurang lebih dikit!'] },
    { id:'hook', name:'Hook', role:'Destruction', hp:1200, atk:220, spd:94, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1109.png', desc:'Bos Moles! Hancurin musuh yang kena Burn.', eEffects:['E1: Skill enhanced nambah DMG 20%','E2: Durasi Burn +1 turn','E3: Skill Lvl +2','E4: Burn nyebar ke sebelah','E5: Ult Lvl +2','E6: DMG ke musuh Burn +20%!'] },
    { id:'guinaifen', name:'Guinaifen', role:'Nihility', hp:1500, atk:220, spd:106, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1210.png', desc:'Firekiss! Musuh kena Burn makin menderita DMG tambahan.', eEffects:['E1: Skill nembus 10% Effect RES','E2: Musuh Burn kena extra Firekiss','E3: Skill Lvl +2','E4: Regen Energy pas burn nancep','E5: Ult Lvl +2','E6: Max tumpukan Firekiss +1!'] },
    { id:'misha', name:'Misha', role:'Destruction', hp:1300, atk:260, spd:96, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1312.png', desc:'Ulti makin banyak hit kalau SP banyak terpakai.', eEffects:['E1: Tiap hit nembus Freeze RES','E2: Hit ulti bisa nurunin DEF musuh','E3: Skill Lvl +2','E4: Ulti DMG multiplier +6% per hit','E5: Ult Lvl +2','E6: Pake ulti dapat SP dan regen Energy!'] },
    { id:'sampo', name:'Sampo', role:'Nihility', hp:1400, atk:180, spd:104, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1108.png', desc:'Ahli Wind Shear! Bikin semua musuh sakit DoT terus-terusan.', eEffects:['E1: Skill mantul +1 kali','E2: Musuh Wind Shear mati, sebelahnya kena juga','E3: Skill Lvl +2','E4: Skill nge-trigger DoT langsung','E5: Ult Lvl +2','E6: Wind Shear DMG multiplier naik!'] },
    { id:'serval', name:'Serval', role:'Erudition', hp:1200, atk:220, spd:104, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1103.png', desc:'AoE Shock mantap! Ulti memperpanjang durasi Shock.', eEffects:['E1: Basic attack nyebar','E2: Regen energy pas nge-hit musuh Shock','E3: Skill Lvl +2','E4: Ulti pasti ngasih Shock ke musuh bebas','E5: Ult Lvl +2','E6: DMG ke musuh Shock +30%!'] },
    { id:'arlan', name:'Arlan', role:'Destruction', hp:1200, atk:220, spd:102, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1008.png', desc:'Serang pake HP, bukan SP! Darah makin dikit, DMG makin gila.', eEffects:['E1: Skill nambah DMG saat HP dibawah 50%','E2: Remove debuff pas ulti','E3: Skill Lvl +2','E4: Kebal mati sekali dan regen HP','E5: Ult Lvl +2','E6: Darah di bawah 50%, Ulti DMG +20% & AoE makin sakit!'] },
    { id:'sushang', name:'Sushang', role:'Hunt', hp:1200, atk:220, spd:107, price:1000, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1206.png', desc:'Sabetan ayam besar! SPD tinggi & mematikan pas musuh Break.', eEffects:['E1: Serang musuh Break gak ngurangin SP','E2: Kurangin DMG masuk setelah kena serangan','E3: Skill Lvl +2','E4: Break Effect +40%','E5: Ult Lvl +2','E6: Advance Forward bisa di-stack!'] },
    { id:'luka', name:'Luka', role:'Nihility', hp:1500, atk:220, spd:103, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1111.png', desc:'Fist of justice! Fokus apply Bleed dan mecahin musuh.', eEffects:['E1: Musuh Bleed kena DMG lebih sakit dari Luka','E2: Skill nambah tumpukan Fighting Will jika kena Physical weakness','E3: Skill Lvl +2','E4: Tiap tumpukan nambah ATK 5%','E5: Ult Lvl +2','E6: Enhanced Basic ATK trigger Bleed berkali-kali!'] },
    { id:'qingque', name:'Qingque', role:'Erudition', hp:1300, atk:260, spd:98, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1204.png', desc:'Judi mahyong pembawa petaka! Draw ubin sampe gila.', eEffects:['E1: Ulti nambah DMG 10%','E2: Pas narik ubin, regen 1 Energy','E3: Skill Lvl +2','E4: 24% peluang Autarky (FUA) abis serang','E5: Ult Lvl +2','E6: Basic ATK mantap kembaliin 1 SP!'] },
    { id:'xueyi', name:'Xueyi', role:'Destruction', hp:1300, atk:260, spd:103, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1214.png', desc:'Karma numpuk saat temen ngurangin Toughness, lalu FUA!', eEffects:['E1: FUA DMG nambah 40%','E2: FUA bisa tembus Weakness apapun dan heal','E3: Skill Lvl +2','E4: Ulti nambah Break Effect 40%','E5: Ult Lvl +2','E6: FUA cuma butuh 6 stack Karma!'] },
    { id:'yukong', name:'Yukong', role:'Harmony', hp:1500, atk:220, spd:107, price:1500, img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/1207.png', desc:'Skill: Bowstrings ATK buff. Ulti: CRIT/CDMG raksasa!', eEffects:['E1: Saat masuk battle, SPD party naik 10%','E2: Tiap ally max Energy, Yukong regen Energy','E3: Skill Lvl +2','E4: Saat Bowstrings aktif, Yukong DMG +30%','E5: Ult Lvl +2','E6: Ulti langsung dapet 1 Bowstrings gratis!'] }
].sort((a,b) => (a.price||0) - (b.price||0));
'''

JS_PART2 = '''
let state = {
    uid:null, stellarJade:0, unlockedIds:[], eidolons:{}, selectedIds:[], party:[], enemies:[],
    targetedEnemyId:0, avQueue:[], currentActor:null, waitingForPlayer:false,
    sp:3, maxSp:5, gameMode:'story', currentStage:1, _casualPrebuiltEnemies:null
};

async function saveUserData() {
    if (!state.uid) return;
    await setDoc(doc(db,'playerSaves',state.uid), {
        userId: state.uid,
        stellarJade:state.stellarJade, unlockedIds:state.unlockedIds,
        highestCasualStage: state.highestCasualStage, playerName: state.playerName, dailyMissions: state.dailyMissions,
        eidolons:state.eidolons, selectedIds:state.selectedIds, currentStage:state.currentStage
    });
    document.getElementById('jade-display').innerText = '💎 ' + state.stellarJade;
    let mj = document.getElementById('menu-jade-display');
    if (mj) mj.innerHTML = '💎 ' + state.stellarJade;
}

async function loadUserData(uid) {
    state.uid = uid;
    const snap = await getDoc(doc(db,'playerSaves',uid));
    if (snap.exists()) {
        let d = snap.data();
        state.stellarJade = d.stellarJade || 2000;
        state.highestCasualStage = d.highestCasualStage || 0;
        state.playerName = d.playerName || state.playerName;
        if (d.dailyMissions && d.dailyMissions.date === new Date().toLocaleDateString()) {
            state.dailyMissions = d.dailyMissions;
        } else {
            state.dailyMissions = { date: new Date().toLocaleDateString(), progress: { playCasual:0, useUlt:0, winBattle:0 }, claimed: [] };
        }
        
        // Fix for previously broken empty names
        if (!d.playerName) {
            await saveUserData(); // block to ensure db is fixed before leaderboard loads
        }
        state.unlockedIds = d.unlockedIds || [...starters];
        state.eidolons = d.eidolons || {};
        state.selectedIds = d.selectedIds || [...starters];
        state.currentStage = d.currentStage || 1;
    } else {
        state.stellarJade = 2000; state.unlockedIds = [...starters];
        state.selectedIds = [...starters]; state.currentStage = 1;
        state.highestCasualStage = 0;
        state.eidolons = {};
        state.dailyMissions = { date: new Date().toLocaleDateString(), progress: { playCasual:0, useUlt:0, winBattle:0 }, claimed: [] };
        await saveUserData();
    }
    state.unlockedIds = [...new Set([...starters,...state.unlockedIds])];
    state.selectedIds = state.selectedIds.filter(id => state.unlockedIds.includes(id));
    if (!state.selectedIds.length) state.selectedIds = [...starters];
    playBGM('menu'); navigateTo('main-menu-view');
    renderCharSelect();
    let mj = document.getElementById('menu-jade-display');
    if (mj) mj.innerHTML = '💎 ' + state.stellarJade;
}

onAuthStateChanged(auth, async (user) => {
    if (user) {
        try {
            state.playerName = user.displayName || user.email.split("@")[0];
            if (user.email === 'admin@myhonkairail.com') { navigateTo('admin-view'); }
            else { await loadUserData(user.uid); }
        } catch (e) {
            alert('Gagal memuat data dari database (Firestore): ' + e.message + '\\n\\nPastikan Firestore Database sudah dibuat di Firebase Console dan Rules-nya allow read/write.');
        }
    } else { navigateTo('login-view'); }
});

document.getElementById('btn-user-login').addEventListener('click', async () => {
    try { await signInWithPopup(auth, new GoogleAuthProvider()); }
    catch(e) { 
        console.error('Login Error:', e); 
        alert('Gagal membuka pop-up login Google: ' + e.message + '\\n\\nPastikan browser tidak memblokir pop-up untuk localhost!');
    }
});

document.getElementById('btn-admin-login').addEventListener('click', async () => {
    try { 
        await signInWithEmailAndPassword(auth, document.getElementById('admin-email').value, document.getElementById('admin-pass').value); 
    }
    catch(e) { 
        alert('Admin Login Gagal: ' + e.message); 
    }
});

window.signOut = (a) => firebaseSignOut(a);
window.loadLeaderboard = async () => {
    try {
        const q = query(collection(db, "playerSaves"), orderBy("highestCasualStage", "desc"), limit(10));
        const querySnapshot = await getDocs(q);
        let html = '';
        let rank = 1;
        querySnapshot.forEach((doc) => {
            let data = doc.data();
            let stg = data.highestCasualStage || 0;
            if (stg > 0) {
                let color = rank===1?'#fbbf24':rank===2?'#94a3b8':rank===3?'#b45309':'#ccc';
                let icon = rank===1?'&#x1F947;':rank===2?'&#x1F948;':rank===3?'&#x1F949;':`#${rank}`;
                html += `<div style="display:flex;justify-content:space-between;background:rgba(255,255,255,0.05);padding:10px 15px;border-radius:8px;border-left:4px solid ${color};">
                    <span style="color:${color};font-weight:bold;">${icon} ${data.playerName || 'Unknown'}</span>
                    <span style="color:#4ade80;">Stage ${stg}</span>
                </div>`;
                rank++;
            }
        });
        if (!html) html = '<div style="text-align:center;color:#888;">Belum ada data</div>';
        document.getElementById('leaderboard-list').innerHTML = html;
    } catch(e) {
        console.error("Leaderboard error:", e);
    }
};


window.playBGM = (type) => {
    document.getElementById('bgm-menu').pause();
    document.getElementById('bgm-battle').pause();
    if(type === 'menu') document.getElementById('bgm-menu').play().catch(e=>console.log(e));
    if(type === 'battle') document.getElementById('bgm-battle').play().catch(e=>console.log(e));
};
window.playSFX = (type) => {
    let a;
    if(type === 'hit') a = document.getElementById('sfx-hit');
    if(type === 'ult') a = document.getElementById('sfx-ult');
    if(type === 'win') a = document.getElementById('sfx-win');
    if(a) { a.currentTime = 0; a.play().catch(e=>console.log(e)); }
};
\n
window.toggleSpeed = () => {
    state.battleSpeed = state.battleSpeed === 1 ? 2 : 1;
    document.getElementById('btn-speed').innerHTML = `&#x23E9; ${state.battleSpeed}x`;
};
window.toggleAuto = () => {
    state.autoBattle = !state.autoBattle;
    document.getElementById('btn-auto').innerHTML = state.autoBattle ? `&#x1F916; Auto: ON` : `&#x1F916; Auto: OFF`;
    document.getElementById('btn-auto').style.background = state.autoBattle ? 'rgba(59,130,246,0.5)' : '';
};
\n
const MISSION_DATA = [
    { id:'playCasual', title:'Main Casual Mode 1x', target: 1, reward: 50 },
    { id:'useUlt', title:'Gunakan Ultimate 3x', target: 3, reward: 50 },
    { id:'winBattle', title:'Menangkan 1 Pertempuran', target: 1, reward: 50 }
];

window.openMissions = () => {
    let html = '';
    MISSION_DATA.forEach(m => {
        let prog = state.dailyMissions.progress[m.id] || 0;
        let isClaimed = state.dailyMissions.claimed.includes(m.id);
        let isDone = prog >= m.target;
        html += `<div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
            <div style="text-align:left;">
                <div style="font-weight:bold;">${m.title}</div>
                <div style="font-size:12px; color:#aaa;">Progres: ${Math.min(prog, m.target)}/${m.target}</div>
            </div>
            <div>
                ${isClaimed ? `<span style="color:#888;">Terklaim</span>` 
                  : isDone ? `<button class="hsr-btn blue" style="padding:5px 10px; font-size:12px;" onclick="claimMission('${m.id}', ${m.reward})">Klaim ${m.reward}&#x1F48E;</button>` 
                  : `<span style="color:#ef4444;">Belum Selesai</span>`}
            </div>
        </div>`;
    });
    document.getElementById('mission-list').innerHTML = html;
    document.getElementById('mission-modal').style.display = 'flex';
};

window.claimMission = async (id, reward) => {
    if (!state.dailyMissions.claimed.includes(id)) {
        state.dailyMissions.claimed.push(id);
        state.stellarJade += reward;
        await saveUserData();
        openMissions();
        document.getElementById('jade-display').innerText = '&#x1F48E; ' + state.stellarJade;
        let mj = document.getElementById('menu-jade-display');
        if (mj) mj.innerHTML = '&#x1F48E; ' + state.stellarJade;
        alert(`Berhasil klaim ${reward} Stellar Jade!`);
    }
};
\n
window.useResonance = async () => {
    if(state.suResonance < 100) return;
    state.suResonance = 0;
    document.getElementById('btn-resonance').innerHTML = `&#x26A1; PATH RESONANCE (0%)`;
    document.getElementById('btn-resonance').style.boxShadow = "0 0 10px var(--accent-orange)";
    
    playSFX("ult");
    writeLog(`&#x26A1; PATH RESONANCE: ${state.suPath.toUpperCase()} ACTIVATE!`, 'system');
    
    if(state.suPath === "Destruction") {
        state.enemies.forEach(e => {
            if(e.hp > 0) { e.hp -= 2000; writeLog(`- Resonance hits ${e.name} for 2000 DMG!`, 'damage'); }
        });
    } else if(state.suPath === "Hunt") {
        let e = state.enemies.find(x => x.hp > 0);
        if(e) { e.hp -= 5000; writeLog(`- Resonance nukes ${e.name} for 5000 DMG!`, 'damage'); }
    } else if(state.suPath === "Abundance") {
        state.party.forEach(p => {
            if(p.hp > 0) {
                p.hp += 2000;
                let m = charDB.find(x=>x.id===p.id).hp;
                if(p.hp > m) p.hp = m;
                writeLog(`- Resonance heals ${p.name} for 2000 HP!`, 'heal');
            }
        });
    }
    
    updateBattleUI();
    checkWinCondition();
};
\nwindow.navigateTo = (v) => {
    if (v === 'main-menu-view') loadLeaderboard();
    document.querySelectorAll('.spa-view').forEach(x => x.classList.remove('active-view'));
    document.getElementById(v).classList.add('active-view');
};
document.getElementById('btn-save-settings').onclick = async () => {
    await setDoc(doc(db,'gameSettings','bossStats'), {
        name:document.getElementById('set-boss-name').value,
        hp:parseInt(document.getElementById('set-boss-hp').value),
        atk:parseInt(document.getElementById('set-boss-dmg').value)
    }); alert('Boss stats updated!');
};

// ===== MODE SELECTION =====
window.goStoryMode = () => { state.gameMode='story'; navigateTo('select-view'); };
window.goCasualMode = () => { state.gameMode='casual'; renderCasualView(); playBGM('menu'); navigateTo('casual-view'); };

window.goSUMode = () => {
    let p = prompt(`Pilih Path Resonance untuk Simulated Universe:
1. Destruction (AoE DMG)
2. Hunt (Single Target Nuke)
3. Abundance (AoE Heal)
Ketik 1, 2, atau 3:`, "1");
    if(p==="1" || p.toLowerCase()==="destruction") state.suPath = "Destruction";
    else if(p==="2" || p.toLowerCase()==="hunt") state.suPath = "Hunt";
    else if(p==="3" || p.toLowerCase()==="abundance") state.suPath = "Abundance";
    else { alert("Dibatalkan."); return; }
    state.suResonance = 0;
 
    if (state.selectedIds.length===0) { alert('Pilih party dulu!'); return; }
    state.gameMode='su'; 
    state.suStage=1; 
    state.suBuffs=[]; 
    state.suPartyHp=null; 
    startSUBattle(); 
};

window.startSUBattle = () => {
    let stageDifficulty = state.suStage * 2;
    let type = state.suStage===5 ? 'boss' : state.suStage===3 ? 'miniboss' : 'kroco';
    let mult = 1 + (stageDifficulty)*0.2;
    let grp = enemyGroups[Math.floor(Math.random()*enemyGroups.length)];
    let scaleE = e => ({ ...e, hp:Math.floor(e.hp*mult), maxHp:Math.floor(e.hp*mult), atk:Math.floor(e.atk*mult), spd:e.spd, statuses:[], energy:0, maxEnergy:100 });
    
    let enemies = [];
    if (type==='boss') enemies = [scaleE(grp.boss), ...grp.minions.map(scaleE)];
    else if (type==='miniboss') enemies = [scaleE({...grp.boss,hp:Math.floor(grp.boss.hp*0.65),atk:Math.floor(grp.boss.atk*0.8),name:'Mini-'+grp.boss.name}), ...grp.minions.slice(0,2).map(scaleE)];
    else enemies = grp.minions.map(scaleE);
    
    startBattle(enemies);
};

window.showSUBuffSelection = () => {
    document.getElementById('su-stage-label').innerText = state.suStage - 1;
    let buffs = [
        {id:'atk', name:'The Hunt: ATK +50%', icon:'\\uD83C\\uDFF9', desc:'Party ATK naik 50% untuk sisa perjalanan.'},
        {id:'spd', name:'The Hunt: SPD +20%', icon:'\\uD83D\\uDCA8', desc:'Party SPD naik 20%, makin sering jalan.'},
        {id:'heal', name:'Abundance: Max HP +25% & Heal', icon:'\\uD83C\\uDF3F', desc:'Party disembuhkan 100% dan Max HP naik 25%.'},
        {id:'energy_start', name:'Erudition: Full Energy', icon:'\\uD83D\\uDCA1', desc:'Mulai battle selalu dengan Ultimate penuh.'},
        {id:'max_sp', name:'Propagation: +2 Max SP', icon:'\\uD83E\\uDDA0', desc:'Kapasitas Maksimal SP bertambah 2.'},
        {id:'enemy_hp', name:'Nihility: Enemy HP -30%', icon:'\\uD83D\\uDC41\\uFE0F', desc:'Musuh kehilangan 30% HP setiap awal battle.'},
        {id:'enemy_slow', name:'Nihility: Enemy Slow', icon:'\\u23F3', desc:'Kecepatan (SPD) musuh berkurang 20%.'},
        {id:'shield', name:'Preservation: Giant Shield', icon:'\\uD83D\\uDEE1\\uFE0F', desc:'Mulai battle dengan Shield 2500 HP untuk seluruh party.'},
        {id:'res_pen', name:'Destruction: RES PEN +25%', icon:'\\uD83D\\uDCA5', desc:'Semua serangan menembus 25% pertahanan musuh.'},
        {id:'berserk', name:'Destruction: Berserker', icon:'\\uD83E\\uDE78', desc:'ATK naik 100%, tapi HP party dipotong 50% tiap awal battle.'}
    ];
    let availableBuffs = buffs.filter(b => !state.suBuffs.includes(b.id));
    let options = availableBuffs.sort(()=>0.5-Math.random()).slice(0,3);
    let html = '';
    options.forEach(b => {
        html += `<button class="hsr-btn" style="text-align:left; padding:15px; border-color:#c026d3;" onclick="selectSUBuff('${b.id}')">
            <div style="font-size:18px; margin-bottom:5px;">${b.icon} ${b.name}</div>
            <div style="font-size:12px; color:#aaa; font-weight:normal;">${b.desc}</div>
        </button>`;
    });
    document.getElementById('su-buff-options').innerHTML = html;
    navigateTo('su-buff-view');
};

window.selectSUBuff = (buffId) => {
    state.suBuffs.push(buffId);
    startSUBattle();
};

function getStageType(s) { if (s%10===0) return 'boss'; if (s%5===0) return 'miniboss'; return 'kroco'; }
function getStageReward(type) { return type==='boss'?300:type==='miniboss'?150:50; }

const enemyGroups = [
    { name:'Automaton Legion', boss:{name:'Automaton Direwolf',hp:4800,atk:210,spd:88,img:'https://ui-avatars.com/api/?name=Automaton+Direwolf&background=552222&color=fff'}, minions:[{name:'Automaton Beetle',hp:900,atk:130,spd:90,img:'https://ui-avatars.com/api/?name=Beetle&background=331111&color=fff'},{name:'Automaton Spider',hp:750,atk:145,spd:95,img:'https://ui-avatars.com/api/?name=Spider&background=331111&color=fff'},{name:'Automaton Grizzly',hp:1100,atk:120,spd:82,img:'https://ui-avatars.com/api/?name=Grizzly&background=331111&color=fff'}] },
    { name:'Antimatter Legion', boss:{name:'Voidranger Trampler',hp:5200,atk:240,spd:85,img:'https://ui-avatars.com/api/?name=Trampler&background=222255&color=fff'}, minions:[{name:'Voidranger Distorter',hp:800,atk:155,spd:92,img:'https://ui-avatars.com/api/?name=Distorter&background=111133&color=fff'},{name:'Voidranger Reaper',hp:950,atk:160,spd:88,img:'https://ui-avatars.com/api/?name=Reaper&background=111133&color=fff'},{name:'Voidranger Eliminator',hp:700,atk:140,spd:98,img:'https://ui-avatars.com/api/?name=Eliminator&background=111133&color=fff'}] },
    { name:'Swarm Disaster',    boss:{name:'Swarm Core',hp:5500,atk:260,spd:80,img:'https://ui-avatars.com/api/?name=Swarm+Core&background=555522&color=fff'},          minions:[{name:'Juvenile Sting',hp:650,atk:135,spd:100,img:'https://ui-avatars.com/api/?name=J+Sting&background=333311&color=fff'},{name:'Bladed Bee',hp:700,atk:150,spd:105,img:'https://ui-avatars.com/api/?name=B+Bee&background=333311&color=fff'},{name:'Leech Fly',hp:550,atk:120,spd:110,img:'https://ui-avatars.com/api/?name=L+Fly&background=333311&color=fff'}] },
    { name:'Stellaron Hunters', boss:{name:'Stellaron Predator',hp:6000,atk:280,spd:92,img:'https://ui-avatars.com/api/?name=Predator&background=552255&color=fff'},   minions:[{name:'Shadowguard',hp:900,atk:170,spd:95,img:'https://ui-avatars.com/api/?name=Shadow&background=331133&color=fff'},{name:'Nullblade',hp:850,atk:180,spd:90,img:'https://ui-avatars.com/api/?name=Null&background=331133&color=fff'},{name:'Veilbreaker',hp:750,atk:165,spd:98,img:'https://ui-avatars.com/api/?name=Veil&background=331133&color=fff'}] },
    { name:'Memory Zone Mares', boss:{name:'Dreamjolt Boss',hp:6500,atk:300,spd:85,img:'https://ui-avatars.com/api/?name=Dreamjolt&background=225555&color=fff'},minions:[{name:'Domebreaker',hp:1000,atk:175,spd:88,img:'https://ui-avatars.com/api/?name=Dome&background=113333&color=fff'},{name:'Stagnant Shadow',hp:900,atk:160,spd:92,img:'https://ui-avatars.com/api/?name=Stagnant&background=113333&color=fff'},{name:'Echo Warden',hp:850,atk:155,spd:95,img:'https://ui-avatars.com/api/?name=Echo&background=113333&color=fff'}] },
    { name:'Abundance Sprite',  boss:{name:'Abundance Supreme',hp:7000,atk:320,spd:80,img:'https://ui-avatars.com/api/?name=Abundance&background=225522&color=fff'},minions:[{name:'Ripple Sprite',hp:1050,atk:180,spd:90,img:'https://ui-avatars.com/api/?name=Ripple&background=113311&color=fff'},{name:'Bloom Sprite',hp:950,atk:165,spd:94,img:'https://ui-avatars.com/api/?name=Bloom&background=113311&color=fff'},{name:'Thorn Sprite',hp:880,atk:170,spd:96,img:'https://ui-avatars.com/api/?name=Thorn&background=113311&color=fff'}] }
];

function getCasualEnemies(stage) {
    let type = getStageType(stage);
    let mult = 1 + Math.floor((stage-1)/10)*0.4;
    let grp = enemyGroups[Math.floor((stage-1)/10) % enemyGroups.length];
    let scaleE = e => ({ ...e, hp:Math.floor(e.hp*mult), maxHp:Math.floor(e.hp*mult), atk:Math.floor(e.atk*mult), spd:e.spd, statuses:[], energy:0, maxEnergy:100 });
    if (type==='boss') return [scaleE(grp.boss), ...grp.minions.map(scaleE)];
    if (type==='miniboss') return [scaleE({...grp.boss,hp:Math.floor(grp.boss.hp*0.65),atk:Math.floor(grp.boss.atk*0.8),name:'Mini-'+grp.boss.name}), ...grp.minions.slice(0,2).map(scaleE)];
    return grp.minions.map(scaleE);
}

function renderCasualView() {
    let s = state.currentStage;
    let type = getStageType(s);
    let reward = getStageReward(type);
    let mult = (1 + Math.floor((s-1)/10)*0.4).toFixed(1);
    let enemies = getCasualEnemies(s);
    state._casualPrebuiltEnemies = enemies;
    document.getElementById('casual-stage-num').textContent = s;
    document.getElementById('casual-stage-num').className = 'stage-number ' + type;
    let badge = document.getElementById('casual-stage-badge');
    badge.textContent = type==='boss'?'BOSS FIGHT!':type==='miniboss'?'MINI-BOSS':'KROCO FIGHT';
    badge.className = 'stage-type-badge ' + type;
    document.getElementById('casual-reward-val').textContent = reward + ' \\u{1F48E}';
    document.getElementById('casual-scale-val').textContent = mult + 'x';
    let chunkStart = Math.floor((s-1)/10)*10+1;
    let barHtml = '';
    for(let i=chunkStart;i<chunkStart+10;i++){
        let stg = getStageType(i);
        let cls = i<s?'done':i===s?'current':stg==='boss'?'boss-dot':stg==='miniboss'?'miniboss-dot':'pending';
        barHtml += `<div class="scb-dot ${cls}" title="Stage ${i}"></div>`;
    }
    document.getElementById('casual-chunk-bar').innerHTML = barHtml;
    let prevHtml = '';
    enemies.forEach((e,idx) => {
        let isBoss = idx===0 && type!=='kroco';
        prevHtml += `<div class="ep-enemy ${isBoss?'boss-preview':''}"><img src="${e.img}" onerror="this.src=\\'https://placehold.co/52x52/1a1a2e/fff?text=E\\'"><span>${e.name}</span></div>`;
    });
    document.getElementById('casual-enemy-preview').innerHTML = prevHtml;
}

window.startCasualBattle = () => {
    if (state.selectedIds.length<1) { alert('Pilih party dulu!'); navigateTo('select-view'); return; }
    state.gameMode='casual';
    let type = getStageType(state.currentStage);
    document.getElementById('battle-title').innerText = `Stage ${state.currentStage} \\u2014 ${type==='boss'?'BOSS FIGHT':type==='miniboss'?'MINI-BOSS':'KROCO'}`;
    startBattle(state._casualPrebuiltEnemies || getCasualEnemies(state.currentStage));
};
'''

JS_PART3 = '''
// ===== CHAR SELECT =====
function renderCharSelect() {
    let grid = document.getElementById('char-roster');
    let roleColors = {'Destruction':'#c084fc','Hunt':'#60a5fa','Erudition':'#f97316','Harmony':'#facc15','Nihility':'#a78bfa','Preservation':'#fb923c','Abundance':'#4ade80','Remembrance':'#67e8f9'};
    let mcData = getMcData();
    grid.innerHTML = charDB.map(c => {
        let isLocked = !state.unlockedIds.includes(c.id);
        let isSel = state.selectedIds.includes(c.id);
        let eLvl = c.id==='mc' ? (state.eidolons[getMcEidolonKey()]||0) : (state.eidolons[c.id]||0);
        let role = c.id==='mc' ? mcData.role : c.role;
        let clr = roleColors[role]||'#fff';
        return `<div class="char-card-select ${isSel?'selected':''} ${isLocked?'locked':''}" onclick="openCharModal('${c.id}')">
            ${eLvl>0?`<span class="eidolon-badge">E${eLvl}</span>`:''}
            <span class="role-badge" style="color:${clr};border-color:${clr};">${role}</span>
            <img class="char-img" src="${c.img}" onerror="this.src='https://placehold.co/75x75/1a1a2e/fff?text=${encodeURIComponent(c.name[0])}'">
            <div style="font-size:11px;font-weight:bold;color:${isLocked?'#666':'#fff'}">${c.name}</div>
            ${isLocked?`<div style="font-size:10px;color:var(--primary-gold)">&#x1F48E; ${c.price||'FREE'}</div>`:''}
        </div>`;
    }).join('');
    let cnt = state.selectedIds.length;
    document.getElementById('party-counter').innerText = `Terpilih: ${cnt}/4`;
    document.getElementById('jade-display').innerText = `\\u{1F48E} ${state.stellarJade}`;
    document.getElementById('btn-start-battle').disabled = cnt<1;
}

window.openPathInfo = () => {
    let html = '<h2>Info Path</h2><hr style="border:1px solid #333;margin:10px 0;">';
    Object.entries(pathInfo).forEach(([k,v]) => {
        html += `<div style="text-align:left;margin-bottom:10px;padding:8px;background:rgba(0,0,0,0.4);border-radius:6px;border-left:3px solid var(--accent-blue);">
            <strong style="color:var(--accent-blue)">${k}</strong><br><span style="font-size:12px;color:#ccc">${v}</span></div>`;
    });
    html += '<button class="hsr-btn" style="width:100%;margin-top:10px;" onclick="closeModal()">Tutup</button>';
    document.getElementById('modal-content-area').innerHTML = html;
    document.getElementById('char-modal').classList.add('active');
};

window.suggestTeam = () => {
    let html = '<h2 style="margin-bottom:8px;">&#x1F4CB; Saran Meta Tim</h2><p style="font-size:12px;color:#888;margin-bottom:8px;">Pilih tim sesuai karakter yang kamu punya.</p><hr style="border:1px solid #333;margin:10px 0;">';
    const teams = [
        {name:'&#x1F7E0; Super Break (MC)', tag:'SUPER BREAK', clr:'#f59e0b', chars:['mc','firefly','ruanmei','gallagher']},
        {name:'&#x1F7E0; Super Break v2',   tag:'SUPER BREAK', clr:'#f59e0b', chars:['mc','rappa','fugue','lingsha']},
        {name:'&#x1F7E0; Boothill Break',   tag:'BREAK',       clr:'#fb923c', chars:['boothill','fugue','ruanmei','gallagher']},
        {name:'&#x1F534; DoT Premium',      tag:'DOT',         clr:'#a855f7', chars:['kafka','blackswan','ruanmei','huohuo']},
        {name:'&#x1F534; DoT Budget',       tag:'DOT',         clr:'#c084fc', chars:['sampo','guinaifen','asta','lynx']},
        {name:'&#x1F534; Hypercarry Acheron',tag:'NUKE',       clr:'#ef4444', chars:['acheron','jiaoqiu','blackswan','gallagher']},
        {name:'&#x1F534; Acheron F2P',      tag:'NUKE',        clr:'#ef4444', chars:['acheron','pela','guinaifen','gallagher']},
        {name:'&#x1F535; FUA Feixiao',      tag:'FUA',         clr:'#3b82f6', chars:['feixiao','moze','robin','aventurine']},
        {name:'&#x1F535; Yunli Counter',    tag:'FUA',         clr:'#6366f1', chars:['yunli','robin','sunday','huohuo']},
        {name:'&#x1F535; Clara Protection', tag:'COUNTER',     clr:'#6366f1', chars:['clara','march7','tingyun','lynx']},
        {name:'&#x1F535; Aglaea Summon',    tag:'SUMMON',      clr:'#a855f7', chars:['aglaea','sunday','ruanmei','huohuo']},
        {name:'&#x1F7E1; Premium FUA',      tag:'FUA',         clr:'#eab308', chars:['topaz','ratio','robin','aventurine']},
        {name:'&#x1F7E1; Jing Yuan FUA',    tag:'FUA',         clr:'#eab308', chars:['jingyuan','sparkle','tingyun','huohuo']},
        {name:'&#x1F7E3; Mono Quantum',     tag:'QUANTUM',     clr:'#d946ef', chars:['seele','silverwolf','sparkle','fuxuan']},
        {name:'&#x1F7E3; Qingque Gambler',  tag:'GAMBLER',     clr:'#d946ef', chars:['qingque','sparkle','silverwolf','fuxuan']},
        {name:'&#x1F535; Jingliu Hyper',    tag:'HYPER',       clr:'#3b82f6', chars:['jingliu','bronya','ruanmei','luocha']},
        {name:'&#x1F7E2; Blade Hyper',      tag:'HYPER',       clr:'#10b981', chars:['blade','bronya','sparkle','luocha']},
        {name:'&#x1F7E1; DHIL Hypercarry',  tag:'HYPER',       clr:'#eab308', chars:['dhil','sparkle','tingyun','huohuo']},
        {name:'&#x1F7E1; Premium Ratio',    tag:'FUA',         clr:'#eab308', chars:['ratio','moze','robin','aventurine']},
        {name:'&#x1F7E3; Herta Kurukuru',   tag:'MEME',        clr:'#14b8a6', chars:['herta','jade','ruanmei','aventurine']},
        {name:'&#x1F7E3; Mono Physical',    tag:'PHYSICAL',    clr:'#9ca3af', chars:['argenti','luka','robin','clara']},
        {name:'&#x1F7E2; Starter F2P',      tag:'F2P',         clr:'#22c55e', chars:['mc','danheng','march7','natasha']}
    ];
    teams.forEach(t => {
        let allOwned = t.chars.every(id => state.unlockedIds.includes(id));
        html += `<div style="text-align:left;margin-bottom:10px;background:rgba(0,0,0,0.4);padding:10px;border-radius:8px;border:1px solid #333;border-left:3px solid ${t.clr};">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
                <strong style="color:#fff">${t.name}</strong>
                <span style="font-size:9px;padding:2px 6px;border-radius:10px;background:${t.clr}22;border:1px solid ${t.clr};color:${t.clr};">${t.tag}</span>
                <span style="font-size:9px;margin-left:auto;color:${allOwned?'#4ade80':'#f87171'}">${allOwned?'&#x2714; Siap':'&#x26A0; Belum Lengkap'}</span>
            </div>
            <div style="display:flex;gap:5px;margin-top:6px;margin-bottom:6px;">`;
        t.chars.forEach(id => {
            let c = charDB.find(x=>x.id===id);
            let owned = state.unlockedIds.includes(id);
            if(c) html += `<img src="${c.img}" style="width:38px;height:38px;border-radius:6px;border:2px solid ${owned?'#4ade80':'#555'};opacity:${owned?1:0.4};" title="${c.name}" onerror="this.src='https://placehold.co/38x38/111/fff?text=?'">`;
        });
        html += `</div><button class="hsr-btn" style="padding:4px 10px;font-size:11px;" onclick="applyTeam('${t.chars.join(',')}')">Pakai Tim Ini</button></div>`;
    });
    html += '<button class="hsr-btn" style="width:100%;margin-top:10px;" onclick="closeModal()">Tutup</button>';
    document.getElementById('modal-content-area').innerHTML = html;
    document.getElementById('char-modal').classList.add('active');
};

window.applyTeam = (listStr) => {
    let chars = listStr.split(',').filter(id => state.unlockedIds.includes(id)).slice(0,4);
    state.selectedIds = chars;
    renderCharSelect(); closeModal();
};

window.openCharModal = (id) => {
    if (id==='mc') {
        let idx = charDB.findIndex(x=>x.id==='mc');
        if (idx!==-1) Object.assign(charDB[idx], getMcData());
    }
    let c = charDB.find(x=>x.id===id);
    if (!c) return;
    let isLocked = !state.unlockedIds.includes(c.id);
    let isSel = state.selectedIds.includes(c.id);
    let eidolonKey = (id==='mc') ? getMcEidolonKey() : id;
    let eLvl = state.eidolons[eidolonKey]||0;
    let ePrice = 500 + (eLvl*300);
    let bonusAtk = Math.floor(c.atk*(eLvl*0.10));
    let bonusHp  = Math.floor(c.hp*(eLvl*0.10));
    let roleColors = {'Destruction':'#c084fc','Hunt':'#60a5fa','Erudition':'#f97316','Harmony':'#facc15','Nihility':'#a78bfa','Preservation':'#fb923c','Abundance':'#4ade80','Remembrance':'#67e8f9'};
    let pathColor = id==='mc' ? (mcPaths[activeMcPath]?.color||'var(--accent-blue)') : (roleColors[c.role]||'var(--accent-blue)');
    let subLabel  = id==='mc' ? `Azriel \\u00B7 ${mcPaths[activeMcPath]?.subname||c.role}` : c.role;

    let mcPathHtml = '';
    if (id==='mc') {
        const pathDefs = [
            {key:'physical',    label:'\\u2694\\uFE0F Destruction', clr:'#c084fc', elem:'Physical'},
            {key:'fire',        label:'\\uD83D\\uDEE1\\uFE0F Preservation', clr:'#fb923c', elem:'Fire'},
            {key:'imaginary',   label:'\\u2B50 Harmony',    clr:'#facc15', elem:'Imaginary'},
            {key:'remembrance', label:'\\u2744\\uFE0F Remembrance', clr:'#67e8f9', elem:'Ice'}
        ];
        mcPathHtml = `<div style="margin-bottom:14px;"><p style="font-size:10px;color:#888;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">PILIH PATH AZRIEL</p><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">`;
        pathDefs.forEach(pd => {
            let active = activeMcPath===pd.key;
            mcPathHtml += `<button onclick="setMcPath('${pd.key}')" style="padding:8px;border-radius:8px;border:2px solid ${active?pd.clr:'#333'};background:${active?pd.clr+'22':'rgba(0,0,0,0.3)'};color:${active?pd.clr:'#aaa'};font-size:11px;font-weight:${active?700:400};cursor:pointer;transition:all 0.2s;">${pd.label}<br><span style="font-size:9px;opacity:0.7;">${pd.elem}</span></button>`;
        });
        mcPathHtml += `</div></div>`;
    }

    let eidolonHtml = '<div class="eidolon-list">';
    (c.eEffects||[]).forEach((ef,idx) => {
        eidolonHtml += `<div class="eidolon-item ${idx<eLvl?'active':''}">${ef}</div>`;
    });
    eidolonHtml += '</div>';

    let actionBtn = '';
    if (isLocked) {
        actionBtn = `<button class="hsr-btn blue" style="width:100%" onclick="buyChar('${c.id}')">Beli &#x1F48E; ${c.price}</button>`;
    } else {
        actionBtn = `<button class="hsr-btn ${isSel?'ult':''}" style="width:100%;margin-bottom:10px;" onclick="toggleChar('${c.id}')">${isSel?'\\u2714 Di-Tim (Batal?)':'\\u2795 Pilih ke Tim'}</button>
        ${eLvl<6?`<button class="hsr-btn" style="width:100%;border-color:var(--jade-pink);color:var(--jade-pink);" onclick="upgradeEidolon('${eidolonKey}',${ePrice})">Upgrade Eidolon E${eLvl+1} &#x1F48E; ${ePrice}</button>`
        :`<button class="hsr-btn" disabled style="width:100%">Max Eidolon (E6) \\u2605</button>`}`;
    }

    document.getElementById('modal-content-area').innerHTML = `
        <img src="${c.img}" style="border:3px solid ${pathColor}44;" onerror="this.src='https://placehold.co/100x100/111/fff?text=${encodeURIComponent(c.name[0])}'">
        <h2 style="margin-bottom:3px">${c.name}${eLvl>0?` <span style="color:var(--primary-gold);font-size:0.8em">E${eLvl}</span>`:''}</h2>
        <p style="color:${pathColor};font-weight:bold;margin-bottom:3px;font-size:13px;">${subLabel}</p>
        <p style="font-size:10px;color:#888;margin-bottom:12px;font-style:italic;">"${pathInfo[c.role]||''}"</p>
        ${mcPathHtml}
        <div style="background:#111;padding:10px;border-radius:6px;margin-bottom:14px;font-size:13px;text-align:left;">
            <div style="display:flex;gap:20px;margin-bottom:8px;">
                <span><strong style="color:#aaa">HP</strong> ${c.hp}<span style="color:var(--heal-green);font-size:11px"> ${bonusHp>0?'+'+bonusHp:''}</span></span>
                <span><strong style="color:#aaa">ATK</strong> ${c.atk}<span style="color:var(--primary-gold);font-size:11px"> ${bonusAtk>0?'+'+bonusAtk:''}</span></span>
                <span><strong style="color:#aaa">SPD</strong> ${c.spd}</span>
            </div>
            <hr style="border:1px solid #222;margin:8px 0;">
            <p style="color:#ccc;font-size:12px;">${c.desc}</p>
        </div>
        ${eidolonHtml}${actionBtn}
        <button class="hsr-btn" style="width:100%;margin-top:10px;" onclick="closeModal()">Tutup</button>`;
    document.getElementById('char-modal').classList.add('active');
};

window.closeModal = () => document.getElementById('char-modal').classList.remove('active');

window.buyChar = async (id) => {
    let c = charDB.find(x=>x.id===id);
    if (state.stellarJade>=c.price) {
        state.stellarJade -= c.price;
        state.unlockedIds.push(id);
        await saveUserData(); renderCharSelect(); openCharModal(id);
    } else alert(`Stellar Jade kurang! Butuh ${c.price}, punya ${state.stellarJade}`);
};

window.upgradeEidolon = async (eidolonKey, price) => {
    if (state.stellarJade>=price) {
        state.stellarJade -= price;
        state.eidolons[eidolonKey] = (state.eidolons[eidolonKey]||0)+1;
        await saveUserData();
        let charId = eidolonKey.startsWith('mc_') ? 'mc' : eidolonKey;
        openCharModal(charId); renderCharSelect();
    } else alert("Stellar Jade kurang buat Eidolon!");
};

window.toggleChar = (id) => {
    if (state.selectedIds.includes(id)) {
        state.selectedIds = state.selectedIds.filter(x=>x!==id);
    } else {
        if (state.selectedIds.length>=4) { alert('Party sudah 4 karakter!'); return; }
        state.selectedIds.push(id);
    }
    renderCharSelect(); closeModal();
};
'''

JS_PART4 = '''
// ===== BATTLE SYSTEM =====
function sleep(ms) { return new Promise(r=>setTimeout(r,ms / (state.battleSpeed || 1))); }

window.startBattle = async function startBattle(prebuiltEnemies) {\n    playBGM('battle');
    state.sp=3; state.maxSp=5; state.waitingForPlayer=false;
    state.avQueue=[]; state.currentActor=null;
    state.targetedEnemyId=0;
    let partyIds = state.selectedIds.slice(0,4);
    if (!partyIds.length) { alert('Pilih party dulu!'); return; }

    // Build party
    state.party = partyIds.map(id => {
        if (id==='mc') {
            let mcData = getMcData();
            let eLvl = state.eidolons[getMcEidolonKey()]||0;
            let bm = 1+eLvl*0.10;
            return { ...mcData, eLvl, maxHp:Math.floor(mcData.hp*bm), hp:Math.floor(mcData.hp*bm), atk:Math.floor(mcData.atk*bm), spd:mcData.spd, shield:0, buffAtk:0, resPen:0, energy:0, maxEnergy:100, statuses:[] };
        }
        let c = charDB.find(x=>x.id===id);
        let eLvl = state.eidolons[id]||0;
        let bm = 1+eLvl*0.10;
        return { ...c, eLvl, maxHp:Math.floor(c.hp*bm), hp:Math.floor(c.hp*bm), atk:Math.floor(c.atk*bm), spd:c.spd, shield:0, buffAtk:0, resPen:0, energy:0, maxEnergy:100, statuses:[] };
    });

    // Robin E2: SPD +16%
    let robin = state.party.find(p=>p.id==='robin');
    if (robin && robin.eLvl>=2) state.party.forEach(p=>{ p.spd=Math.round(p.spd*1.16); });
    // Huohuo E1: SPD +12%
    let huohuo = state.party.find(p=>p.id==='huohuo');
    if (huohuo && huohuo.eLvl>=1) state.party.forEach(p=>{ p.spd=Math.round(p.spd*1.12); });

    // Build enemies
    let storyEnemies = prebuiltEnemies || (() => {
        let grp = enemyGroups[Math.floor(Math.random()*enemyGroups.length)];
        return [
            {...grp.boss, maxHp:grp.boss.hp, hp:grp.boss.hp, statuses:[], energy:0, maxEnergy:100},
            ...grp.minions.map(m=>({...m, maxHp:m.hp, hp:m.hp, statuses:[], energy:0, maxEnergy:100}))
        ];
    })();
    state.enemies = prebuiltEnemies ? prebuiltEnemies.map((e,i)=>({...e,id:'e'+i,maxHp:e.hp})) : storyEnemies.map((e,i)=>({...e,id:'e'+i,maxHp:e.hp||e.hp}));
    state.targetedEnemyId = state.enemies[0].id;

    if (state.gameMode === 'su' && state.suPartyHp) {
        state.party.forEach(p => {
            let saved = state.suPartyHp[p.id];
            if (saved) { p.hp = saved.hp; p.energy = saved.energy; }
        });
        if (state.suBuffs.includes('atk')) state.party.forEach(p => p.buffAtk = (p.buffAtk||0) + 0.5);
        if (state.suBuffs.includes('spd')) state.party.forEach(p => p.spd = Math.floor(p.spd * 1.2));
        if (state.suBuffs.includes('energy_start')) state.party.forEach(p => p.energy = p.maxEnergy);
        if (state.suBuffs.includes('max_sp')) state.maxSp += 2;
        if (state.suBuffs.includes('heal')) state.party.forEach(p => { p.maxHp = Math.floor(p.maxHp*1.25); p.hp = p.maxHp; });
        if (state.suBuffs.includes('enemy_hp')) state.enemies.forEach(e => { e.maxHp = Math.floor(e.maxHp*0.7); e.hp = e.maxHp; });
        if (state.suBuffs.includes('enemy_slow')) state.enemies.forEach(e => e.spd = Math.floor(e.spd * 0.8));
        if (state.suBuffs.includes('shield')) state.party.forEach(p => p.shield = 2500);
        if (state.suBuffs.includes('res_pen')) state.party.forEach(p => p.resPen = (p.resPen||0) + 0.25);
        if (state.suBuffs.includes('berserk')) state.party.forEach(p => { p.buffAtk = (p.buffAtk||0) + 1.0; p.hp = Math.floor(p.hp*0.5) || 1; });
    }


    // Build AV queue (Action Value)
    state.avQueue = [
        ...state.party.filter(p=>p.hp>0).map(p=>({id:p.id,av:Math.floor(10000/p.spd),isPlayer:true})),
        ...state.enemies.map(e=>({id:e.id,av:Math.floor(10000/e.spd),isPlayer:false}))
    ];
    
    if (state.party.find(p=>p.id==='jingyuan')) state.avQueue.push({id:'ll', av:Math.floor(10000/60), isSummon:true, isPlayer:true, ownerId:'jingyuan'});
    if (state.party.find(p=>p.id==='lingsha')) state.avQueue.push({id:'fuyuan', av:Math.floor(10000/90), isSummon:true, isPlayer:true, ownerId:'lingsha'});
    if (state.party.find(p=>p.id==='topaz')) state.avQueue.push({id:'numby', av:Math.floor(10000/80), isSummon:true, isPlayer:true, ownerId:'topaz'});
    if (state.party.find(p=>p.id==='aglaea')) state.avQueue.push({id:'garmentmaker', av:Math.floor(10000/90), isSummon:true, isPlayer:true, ownerId:'aglaea'});

    state.avQueue.sort((a,b)=>a.av-b.av);

    navigateTo('user-view');
    document.getElementById('battle-log').innerHTML='';
    document.getElementById('su-resonance-container').style.display = state.gameMode==="su" ? "block" : "none";
    writeLog('=== PERTEMPURAN DIMULAI! ===','system');
    renderBattle(); renderActionOrderBar();
    await sleep(500); advanceTurn();
}

function renderBattle() {
    let pu = document.getElementById('player-ui');
    let eu = document.getElementById('enemy-ui');
    pu.innerHTML = state.party.map(p => {
        let hpPct = Math.max(0,Math.min(100,(p.hp/p.maxHp)*100));
        let shPct = p.shield>0 ? Math.max(0,Math.min(100,(p.shield/(p.maxHp*0.3))*100)) : 0;
        let enPct = (p.energy/p.maxEnergy)*100;
        let statIcons = (p.statuses||[]).map(s=>s.icon||'?').join('');
        let isAct = state.currentActor && state.currentActor.id===p.id && state.currentActor.isPlayer;
        return `<div class="entity-card ${isAct?'active-turn':''} ${p.hp<=0?'dead':''}" id="card-${p.id}">
            <img class="entity-img" src="${p.img}" onerror="this.src='https://placehold.co/55x55/111/fff?text=?'">
            <div class="info-box">
                <div style="font-size:12px;font-weight:bold;color:${p.hp<=0?'#555':'#fff'}">${p.name}${p.eLvl>0?` <span style="color:var(--primary-gold);font-size:10px">E${p.eLvl}</span>`:''}</div>
                <div style="font-size:10px;color:#888">${p.role}</div>
                <div class="bar-container"><div class="hp-bar" style="width:${hpPct}%"></div><div class="shield-bar" style="width:${shPct}%"></div></div>
                <div style="font-size:10px;color:#aaa">${p.hp}/${p.maxHp}${p.shield>0?` <span style="color:var(--shield-white)">[\\uD83D\\uDEE1 ${p.shield}]</span>`:''}</div>
                <div class="energy-container"><div class="energy-bar" style="width:${enPct}%"></div></div>
                <div class="status-tray">${statIcons?`<span class="status-icon">${statIcons}</span>`:''}</div>
            </div></div>`;
    }).join('');
    eu.innerHTML = state.enemies.map(e => {
        let hpPct = Math.max(0,Math.min(100,(e.hp/e.maxHp)*100));
        let isTarget = e.id===state.targetedEnemyId;
        let hasDebuff = (e.statuses||[]).length>0;
        let dripIcons = (e.statuses||[]).map(s=>s.icon||'').filter(Boolean).slice(0,3);
        let isAct = state.currentActor && state.currentActor.id===e.id && !state.currentActor.isPlayer;
        return `<div class="entity-card enemy ${isTarget?'targeted':''} ${isAct?'active-turn':''} ${e.hp<=0?'dead':''} ${hasDebuff?'has-debuff':''}" id="card-${e.id}" onclick="setTarget('${e.id}')">
            ${hasDebuff?`<div class="debuff-drip">${dripIcons.map(i=>`<span>${i}</span>`).join('')}</div>`:''}
            <img class="entity-img" src="${e.img}" onerror="this.src='https://placehold.co/55x55/1a1a2e/fff?text=E'">
            <div class="info-box">
                <div style="font-size:12px;font-weight:bold">${e.name}</div>
                <div class="bar-container"><div class="hp-bar enemy-bar" style="width:${hpPct}%"></div></div>
                <div style="font-size:10px;color:#aaa">${e.hp}/${e.maxHp}</div>
                <div class="status-tray">${(e.statuses||[]).map(s=>`<span class="status-icon" style="color:var(--debuff-purple)">${s.icon||s.name[0]}</span>`).join('')}</div>
            </div></div>`;
    }).join('');
}

function renderActionOrderBar() {
    let bar = document.getElementById('action-order-bar');
    let items = state.avQueue.slice(0,12).map((av,i) => {
        let ent;
        if (av.isSummon) {
            let sName = av.id==='mem'?'Mem':av.id==='ll'?'Lightning Lord':av.id==='fuyuan'?'Fuyuan':av.id==='numby'?'Numby':av.id==='garmentmaker'?'Garmentmaker':'Summon';
            ent = {name:sName, img:'https://ui-avatars.com/api/?name='+sName.replace(' ','+')+'&background=87ceeb&color=fff'};
        }
        else ent = av.isPlayer ? state.party.find(p=>p.id===av.id) : state.enemies.find(e=>e.id===av.id);
        if (!ent) return '';
        let isCur = i===0 && state.currentActor && state.currentActor.id===av.id;
        return `<div class="aob-item ${av.isPlayer?'is-player':'is-enemy'} ${isCur?'current':''}">
            <img src="${ent.img}" onerror="this.src='https://placehold.co/36x36/111/fff?text=?'" title="${ent.name}">
            <span>${ent.name.split(' ')[0]}</span></div>
        ${i<Math.min(11,state.avQueue.length-1)?'<span class="aob-arrow">&#x276F;</span>':''}`;
    }).join('');
    bar.innerHTML = '<span id="aob-label">ORDER</span>' + items;
}

window.setTarget = (id) => {
    let e = state.enemies.find(x=>x.id===id);
    if (e && e.hp>0) { state.targetedEnemyId=id; renderBattle(); }
};

function writeLog(msg, type='') {
    let log = document.getElementById('battle-log');
    log.innerHTML += `<div class="log-entry ${type}">${msg}</div>`;
    log.scrollTop = log.scrollHeight;
}

async function animateAttack(attackerId, targetId, isEnemy) {
    playSFX("hit");
    let attackerCard = document.getElementById('card-'+attackerId);
    let targetCard   = document.getElementById('card-'+targetId);
    if (!attackerCard || !targetCard) return;
    attackerCard.classList.add(isEnemy?'is-attacking-enemy':'is-attacking');
    await sleep(150);
    targetCard.classList.add('is-damaged');

    // Slash burst on target
    let tRect = targetCard.getBoundingClientRect();
    let burst = document.createElement('div');
    burst.className = 'slash-burst-anim';
    burst.style.cssText = `left:${tRect.left+tRect.width/2}px;top:${tRect.top+tRect.height/2}px;`;
    burst.innerHTML = `<img src="https://png.pngtree.com/png-vector/20231103/ourmid/pngtree-slashing-sword-effect-png-image_10457639.png" style="transform:translate(-50%,-50%);">`;
    document.body.appendChild(burst);

    setTimeout(()=>{ attackerCard.classList.remove('is-attacking','is-attacking-enemy'); targetCard.classList.remove('is-damaged'); burst.remove(); }, 500);
    await sleep(300);
}

function showFX(targetId, type) {
    let card = document.getElementById('card-'+targetId);
    if (!card) return;
    let fx = document.createElement('div');
    let fxParticles = {heal:'\\u2665\\u2665\\u2665', shield:'\\uD83D\\uDEE1\\uD83D\\uDEE1\\uD83D\\uDEE1', debuff:'\\u2620\\u2620\\u2620', buff:'\\u2B50\\u2B50\\u2B50'};
    fx.className = type+'-burst-fx';
    card.appendChild(fx);
    // Floating particles
    let parts = fxParticles[type]||'';
    for(let i=0;i<3;i++){
        let p=document.createElement('div');
        p.className='fx-particle';
        p.textContent=parts[i]||'\\u2728';
        p.style.cssText=`left:${20+i*25}%;top:${10+Math.random()*30}%;animation-delay:${i*0.15}s;`;
        card.appendChild(p);
        setTimeout(()=>p.remove(),1200);
    }
    card.classList.add('is-'+type==='heal'?'healing':'buffed');
    setTimeout(()=>{ fx.remove(); card.classList.remove('is-healing','is-buffed'); },900);
}

function showDmgPopup(targetId, dmg, color='#fff') {
    let card = document.getElementById('card-'+targetId);
    if (!card) return;
    let pop = document.createElement('div');
    pop.className='dmg-popup';
    pop.style.color=color;
    pop.textContent=dmg;
    card.appendChild(pop);
    setTimeout(()=>pop.remove(),900);
}

function calcDmg(atk, mult, resPen, extraBuff) {
    let dmg = Math.floor(atk * (mult/100) * (1+(resPen||0)) * (1+(extraBuff||0)));
    return Math.max(1, dmg + Math.floor(Math.random()*Math.max(1,dmg*0.1)));
}

function applyDmgToEnemy(enemy, dmg, logColor) {
    enemy.hp = Math.max(0, enemy.hp-dmg);
    showDmgPopup(enemy.id, '-'+dmg, logColor||'#ff6b6b');
}

function healAlly(ally, amt) {
    ally.hp = Math.min(ally.maxHp, ally.hp+amt);
    showFX(ally.id, 'heal');
    showDmgPopup(ally.id, '+'+amt, 'var(--heal-green)');
}

function shieldAlly(ally, amt) {
    ally.shield = Math.min(ally.maxHp, (ally.shield||0)+amt);
    showFX(ally.id, 'shield');
    showDmgPopup(ally.id, '\\uD83D\\uDEE1 +'+amt, 'var(--shield-white)');
}
'''

JS_PART5 = '''
async function advanceTurn() {
    if (state.waitingForPlayer) return;
    // Clean dead from queue
    state.avQueue = state.avQueue.filter(av => {
        if (av.isSummon) return true;
        if (av.isPlayer) return state.party.find(p=>p.id===av.id && p.hp>0);
        return state.enemies.find(e=>e.id===av.id && e.hp>0);
    });
    if (!state.avQueue.length) { endGame(false); return; }

    let actor = state.avQueue[0];
    state.currentActor = actor;
    // Advance AV
    let minAv = actor.av;
    state.avQueue.forEach(av=>av.av-=minAv);

    if (actor.isSummon && actor.isPlayer) {
        document.getElementById('action-menu').style.display='none';
        renderBattle(); renderActionOrderBar();
        await sleep(600);
        
        let aliveEnemies = state.enemies.filter(e=>e.hp>0);
        if (aliveEnemies.length > 0) {
            let target = aliveEnemies[Math.floor(Math.random() * aliveEnemies.length)];
            let ownerId = actor.ownerId || 'mc';
            let owner = state.party.find(p=>p.id===ownerId) || {atk:1500};
            let baseAtk = owner.atk;
            
            if (actor.id === 'mem') {
                let dmg = calcDmg(baseAtk, 150, 0, 0);
                applyDmgToEnemy(target, dmg, '#87ceeb');
                writeLog(`\\u2744\\uFE0F Mem menyerang ${target.name}: -${dmg} DMG!`, 'player-atk');
                
                state.memEnergy = (state.memEnergy || 0) + 30;
                if (state.memEnergy >= 100) {
                    state.memEnergy = 0;
                    let aliveAllies = state.party.filter(p=>p.hp>0);
                    if (aliveAllies.length > 0) {
                        let buffed = aliveAllies[Math.floor(Math.random() * aliveAllies.length)];
                        buffed.resPen = (buffed.resPen || 0) + 0.3;
                        showFX(buffed.id, 'buff');
                        writeLog(`\\u2728 Mem Energi Penuh! Memberikan Buff True Damage (30% Res Pen) ke ${buffed.name}!`, 'player-atk');
                    }
                }
            } else if (actor.id === 'll') {
                let dmg = calcDmg(baseAtk, 250, 0, 0);
                writeLog(`\\u26A1 Lightning Lord ngelepas stack ke musuh deal ${dmg} AoE DMG!`, 'player-atk');
                state.enemies.filter(e=>e.hp>0).forEach(e => { applyDmgToEnemy(e, dmg, '#eab308'); });
            } else if (actor.id === 'fuyuan') {
                let dmg = calcDmg(baseAtk, 100, 0, 0);
                let healAmt = Math.floor(baseAtk * 0.5);
                writeLog(`\\uD83D\\uDC07 Fuyuan nyerang deal ${dmg} DMG dan nge-heal tim ${healAmt} HP!`, 'player-atk');
                state.enemies.filter(e=>e.hp>0).forEach(e => { applyDmgToEnemy(e, dmg, '#ef4444'); });
                state.party.filter(p=>p.hp>0).forEach(p => { p.hp = Math.min(p.maxHp, p.hp + healAmt); showFX(p.id, 'heal'); });
            } else if (actor.id === 'numby') {
                let dmg = calcDmg(baseAtk, 200, 0, 0);
                applyDmgToEnemy(target, dmg, '#f97316');
                writeLog(`\\uD83D\\uDC3D Numby muter-muter nyerang ${target.name} deal ${dmg} DMG!`, 'player-atk');
            } else if (actor.id === 'garmentmaker') {
                let dmg = calcDmg(baseAtk, 180, 0, 0);
                applyDmgToEnemy(target, dmg, '#a855f7');
                writeLog(`\\uD83D\\uDC57 Garmentmaker beraksi deal ${dmg} DMG ke ${target.name}!`, 'player-atk');
            }
        }
        finishTurn();
        return;
    }

    if (actor.isPlayer) {
        let member = state.party.find(p=>p.id===actor.id && p.hp>0);
        if (!member) { finishTurn(); return; }
        renderBattle(); renderActionOrderBar();
        document.getElementById('active-char-name').innerText = `Giliran: ${member.name}`;
        document.getElementById('active-char-desc').innerText = member.desc||'';
        // Update SP dots
        let spHtml='';
        for(let i=0;i<state.maxSp;i++) spHtml+=`<div class="sp-dot ${i<state.sp?'active':''}"></div>`;
        document.getElementById('sp-display').innerHTML=spHtml;
        document.getElementById('btn-skill').disabled = state.sp<1;
        document.getElementById('btn-ult').disabled = member.energy<member.maxEnergy;
        document.getElementById('action-menu').style.display='flex';
        state.waitingForPlayer=true;
        
        // Auto Battle Intercept
        if (state.autoBattle) {
            setTimeout(async () => {
                let member = state.party.find(p=>p.id===state.currentActor.id && p.hp>0);
                if (member && member.energy >= member.maxEnergy) {
                    await playerAction('ultimate');
                    return;
                }
                let type = (state.sp >= 1 && Math.random() > 0.3) ? 'skill' : 'basic';
                playerAction(type);
            }, 800 / (state.battleSpeed || 1));
            return;
        }
    } else {
        let enemy = state.enemies.find(e=>e.id===actor.id && e.hp>0);
        if (!enemy) { finishTurn(); return; }
        document.getElementById('action-menu').style.display='none';
        renderBattle(); renderActionOrderBar();
        await sleep(600);
        await enemyTurn(enemy);
    }
}

async function enemyTurn(enemy) {
    // Apply DoT to enemy first (check timing - actually apply at start of enemy turn)
    for(let st of (enemy.statuses||[])) {
        if (st.type==='dot' && st.dmg) {
            let dotDmg = st.dmg;
            enemy.hp = Math.max(0, enemy.hp-dotDmg);
            showDmgPopup(enemy.id, '\\u2620 -'+dotDmg, 'var(--debuff-purple)');
            writeLog(`\\u2620 ${enemy.name} kena DoT ${st.name}: -${dotDmg} HP`, 'enemy-atk');
            await sleep(400);
            renderBattle();
            if (enemy.hp<=0) { finishTurn(); return; }
        }
    }
    // Reduce status durations
    if (enemy.statuses) {
        enemy.statuses = enemy.statuses.map(s=>({...s, duration:(s.duration||1)-1})).filter(s=>s.duration>0);
    }

    // Pick living ally target
    let targets = state.party.filter(p=>p.hp>0);
    if (!targets.length) { endGame(false); return; }
    let target = targets[Math.floor(Math.random()*targets.length)];

    await animateAttack(enemy.id, target.id, true);

    let dmg = Math.floor(enemy.atk*(0.8+Math.random()*0.4));
    // Absorb with shield first
    if (target.shield>0) {
        let absorbed = Math.min(target.shield, dmg);
        target.shield -= absorbed; dmg -= absorbed;
        if (absorbed>0) { showDmgPopup(target.id, '\\uD83D\\uDEE1 -'+absorbed, 'var(--shield-white)'); await sleep(200); }
    }
    if (dmg>0) {
        target.hp = Math.max(0, target.hp-dmg);
        showDmgPopup(target.id, '-'+dmg, 'var(--danger-red)');
    }
    writeLog(`${enemy.name} menyerang ${target.name}: -${dmg} HP`, 'enemy-atk');
    enemy.energy = Math.min(enemy.maxEnergy, (enemy.energy||0)+15);

    // Bailu pasif: auto heal when ally hit
    let bailu = state.party.find(p=>p.id==='bailu'&&p.hp>0);
    if (bailu && target.hp/target.maxHp<0.5) { let h=Math.floor(bailu.atk*0.5); healAlly(target,h); writeLog(`\\u{1F48A} Bailu pasif: Heal ${target.name} +${h} HP`,'player-atk'); }

    // Yunli counter when hit
    let yunli = state.party.find(p=>p.id==='yunli'&&p.hp>0);
    if (yunli && Math.random()<0.6) {
        await sleep(300);
        let cDmg = calcDmg(yunli.atk, 320, yunli.resPen, 0);
        applyDmgToEnemy(enemy, cDmg);
        writeLog(`\\u26A1 Yunli Counter: -${cDmg} DMG ke ${enemy.name}`, 'player-atk');
        if (enemy.hp<=0) { writeLog(`\\u2620 ${enemy.name} dikalahkan!`, 'system'); finishTurn(); return; }
    }

    renderBattle();
    await sleep(300);
    finishTurn();
}

window.playerAction = async (action) => {
    if (!state.waitingForPlayer) return;
    state.waitingForPlayer=false;
    document.getElementById('action-menu').style.display='none';

    let member = state.party.find(p=>p.id===state.currentActor.id && p.hp>0);
    if (!member) { finishTurn(); return; }

    // Skill SP check
    if (action==='skill' && state.sp<1) { state.waitingForPlayer=true; document.getElementById('action-menu').style.display='flex'; alert('SP tidak cukup!'); return; }
    if (action==='ultimate' && member.energy<member.maxEnergy) { state.waitingForPlayer=true; document.getElementById('action-menu').style.display='flex'; alert('Energy belum penuh!'); return; }

    // SP update
    if (action==='basic') { state.sp=Math.min(state.maxSp, state.sp+1); member.energy=Math.min(member.maxEnergy, member.energy+20); }
    else if (action==='skill') { state.sp=Math.max(0, state.sp-1); member.energy=Math.min(member.maxEnergy, member.energy+30); }
    else if (action==='ultimate') { member.energy=0; if(state.dailyMissions) state.dailyMissions.progress.useUlt=(state.dailyMissions.progress.useUlt||0)+1; }

    let target = state.enemies.find(e=>e.id===state.targetedEnemyId && e.hp>0);
    if (!target) { target=state.enemies.find(e=>e.hp>0); }
    if (!target && !['march7','natasha','luocha','gallagher','lingsha','bronya','tingyun','sparkle','fuxuan','gepard','huohuo','fugue','sunday'].includes(member.id)) {
        endGame(true); return;
    }

    await animateAttack(member.id, target?target.id:'', false);

    let id = member.id;
    let eLvl = member.eLvl||0;
    let dmg=0, healed=false;

    // Character actions
    if (id==='natasha'||id==='luocha'||id==='bailu'||id==='huohuo'||id==='gallagher'||id==='lingsha') {
        // Healers
        let healAmt = action==='ultimate'? Math.floor(member.atk*1.5 + 1200) : action==='skill'? Math.floor(member.atk*1.0 + 800) : Math.floor(member.atk*0.5 + 400);
        let healTargets = action==='basic' ? [state.party.filter(p=>p.hp>0).sort((a,b)=>a.hp-b.hp)[0]] : state.party.filter(p=>p.hp>0);
        healTargets.forEach(p=>healAlly(p, healAmt));
        writeLog(`\\u{1FA7A} ${member.name} ${action}: Heal +${healAmt} HP`, 'player-atk');
        if (id==='huohuo' && action==='ultimate') {
            state.party.filter(p=>p.hp>0).forEach(p=>{ 
                p.buffAtk=(p.buffAtk||0)+0.3; 
                p.energy=Math.min(p.maxEnergy, p.energy+(p.maxEnergy*0.2));
                showFX(p.id, 'heal');
            });
            writeLog('\\u{1F47B} Huohuo Ult: ATK Buff +30% & 20% Energy Regen ke seluruh party!','system');
            if(eLvl>=1) { state.party.forEach(p=>{ p.spd=Math.round(p.spd*1.12); }); writeLog('Huohuo E1: SPD Tim +12%!','system'); }
        }
        if (id==='gallagher' && target) {
            let debuffAmt=0.2; target.statuses=target.statuses||[];
            target.statuses.push({name:'Besotted',type:'weakness',icon:'\\uD83C\\uDF7A',duration:2,defShred:debuffAmt});
            showFX(target.id,'debuff'); writeLog(`\\uD83C\\uDF7A Gallagher: Besotted musuh -${debuffAmt*100}% Break DMG RES`,'player-atk');
        }
        healed=true;
    } else if (id==='march7') {
        if (action==='basic') { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
        else if (action==='skill') { let shieldTarget=state.party.filter(p=>p.hp>0).sort((a,b)=>{let sa=a.shield>0?1:0,sb=b.shield>0?1:0;return sa!==sb?sa-sb:(a.hp/a.maxHp)-(b.hp/b.maxHp);})[0]; let shAmt=Math.floor(member.atk*1.2+1000); shieldAlly(shieldTarget,shAmt); writeLog(`\\uD83D\\uDEE1 March: Shield +${shAmt} ke ${shieldTarget.name}`,'player-atk'); }
        else { dmg=calcDmg(member.atk,300,member.resPen,member.buffAtk); }
    } else if (id==='gepard') {
        if (action==='ultimate') { let shAmt=Math.floor(member.atk*0.8+1800); state.party.filter(p=>p.hp>0).forEach(p=>shieldAlly(p,shAmt)); writeLog(`\\uD83D\\uDEE1 Gepard Ult: Shield AoE +${shAmt}!`,'player-atk'); }
        else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='fuxuan') {
        if (action==='skill') { let mitAmt=0.15; state.party.filter(p=>p.hp>0).forEach(p=>{p.resPen=(p.resPen||0)+mitAmt;}); writeLog('\\u2638\\uFE0F Fu Xuan Matrix: Mitigasi +15% tim!','system'); }
        else { dmg=calcDmg(member.atk, action==='ultimate'?200:80, member.resPen, member.buffAtk); }
    } else if (id==='aventurine') {
        if (action==='skill') { state.party.filter(p=>p.hp>0).forEach(p=>shieldAlly(p,Math.floor(member.atk*0.8+800))); writeLog('\\uD83C\\uDFB2 Aventurine: Shield Party!','player-atk'); }
        else { dmg=calcDmg(member.atk, action==='ultimate'?350:80, member.resPen, member.buffAtk); }
    } else if (id==='bronya') {
        if (action==='skill') { let buffed=state.party.filter(p=>p.hp>0&&p.id!==id)[0]; if(buffed){buffed.buffAtk=(buffed.buffAtk||0)+0.6; writeLog(`\\u2728 Bronya Skill: ${buffed.name} ATK +60%`,'player-atk');} }
        else if (action==='ultimate') { state.party.filter(p=>p.hp>0).forEach(p=>{p.buffAtk=(p.buffAtk||0)+0.6;}); writeLog('\\u2728 Bronya Ult: ATK Buff +60% Party!','system'); }
        else { dmg=calcDmg(member.atk,80,member.resPen,member.buffAtk); }
    } else if (id==='tingyun') {
        if (action==='skill') { let buffed=state.party.filter(p=>p.hp>0&&p.id!==id).sort((a,b)=>b.atk-a.atk)[0]; if(buffed){buffed.buffAtk=(buffed.buffAtk||0)+0.8; showFX(buffed.id,'buff'); writeLog(`\\u2728 Tingyun Skill: ${buffed.name} ATK +80%`,'player-atk');} }
        else if (action==='ultimate') { let t2=state.party.filter(p=>p.hp>0&&p.id!==id)[0]; if(t2){t2.energy=Math.min(t2.maxEnergy,t2.energy+60); showFX(t2.id,'buff'); writeLog(`\\u26A1 Tingyun Ult: ${t2.name} +60 Energy!`,'player-atk');} }
        else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='sparkle') {
        if (action==='skill') { state.sp=Math.min(state.maxSp, state.sp+2); let t3=state.party.filter(p=>p.hp>0&&p.id!==id).sort((a,b)=>b.atk-a.atk)[0]; if(t3){t3.buffAtk=(t3.buffAtk||0)+0.5; showFX(t3.id,'buff');} writeLog('\\uD83C\\uDFAD Sparkle Skill: +2 SP & ATK Buff!','player-atk'); }
        else if (action==='ultimate') { state.sp=state.maxSp; writeLog('\\uD83C\\uDFAD Sparkle Ult: SP MAX!','system'); state.party.filter(p=>p.hp>0).forEach(p=>showFX(p.id,'buff')); }
        else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='robin') {
        if (action==='ultimate') {
            state.party.filter(p=>p.hp>0&&p.id!==id).forEach(p=>{p.buffAtk=(p.buffAtk||0)+1.0; showFX(p.id,'buff');});
            writeLog('\\uD83D\\uDD4A\\uFE0F Robin Ult: ATK +100% Party! Action Advance!','system');
        } else { dmg=calcDmg(member.atk, action==='skill'?160:100, member.resPen, member.buffAtk); }
    } else if (id==='sunday') {
        if (action==='skill'||action==='ultimate') {
            let dps=state.party.filter(p=>p.hp>0&&p.id!==id).sort((a,b)=>b.atk-a.atk)[0];
            if(dps){
                if (action === 'ultimate') {
                    dps.buffAtk=(dps.buffAtk||0)+1.0; 
                    dps.energy=Math.min(dps.maxEnergy, dps.energy+(dps.maxEnergy*0.3));
                } else {
                    dps.buffAtk=(dps.buffAtk||0)+0.4;
                }
                showFX(dps.id,'buff'); 
                if(eLvl>=2)state.sp=Math.min(state.maxSp,state.sp+1);

                let dpsAvEntry = state.avQueue.find(av => av.id === dps.id);
                if (dpsAvEntry) dpsAvEntry.av = state.currentActor.av;

                let summonAvEntry = state.avQueue.find(av => av.isSummon && (av.ownerId === dps.id || (dps.id==='mc' && av.id==='mem')));
                if (summonAvEntry) summonAvEntry.av = state.currentActor.av;
            }
            if (action === 'ultimate') {
                writeLog(`\\uD83D\\uDD4A\\uFE0F Sunday Ulti: Buff Hypercarry (40% CR, 60% CDMG, 30% Energy) & 100% Action Forward ke ${dps?.name||'DPS'} (serta Khodamnya)!`,'player-atk');
            } else {
                writeLog(`\\uD83D\\uDD4A\\uFE0F Sunday Skill: CRIT DMG Buff & 100% Action Forward ke ${dps?.name||'DPS'} (serta Khodamnya)!`,'player-atk');
            }
        } else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='ruanmei') {
        if (action==='skill'||action==='ultimate') {
            state.party.filter(p=>p.hp>0).forEach(p=>{p.resPen=(p.resPen||0)+0.25; p.buffAtk=(p.buffAtk||0)+0.3;});
            writeLog('\\u2728 Ruan Mei: RES PEN +25% & ATK +30% Party!','system');
            showFX(member.id,'buff');
        } else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='fugue') {
        if (action==='skill'||action==='ultimate') {
            if(target){
                let toughReduce=Math.floor(member.atk*0.3); target.statuses=target.statuses||[];
                target.statuses.push({name:'Fie Xiao',type:'weakness',icon:'\\uD83D\\uDD76\\uFE0F',duration:2,dmg:toughReduce});
                showFX(target.id,'debuff');
            }
            state.party.filter(p=>p.hp>0).forEach(p=>{p.buffAtk=(p.buffAtk||0)+0.15;});
            writeLog('\\uD83D\\uDD76\\uFE0F Fugue: Super Break Amp + Toughness Shred!','player-atk');
        } else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
    } else if (id==='kafka') {
        dmg=calcDmg(member.atk, action==='ultimate'?200:150, member.resPen, member.buffAtk);
        if (target) {
            target.statuses=target.statuses||[];
            let shock={name:'Shock',type:'dot',icon:'\\u26A1',duration:3,dmg:Math.floor(member.atk*0.6)};
            if (!target.statuses.find(s=>s.name==='Shock')) target.statuses.push(shock);
            else { let s=target.statuses.find(x=>x.name==='Shock'); s.duration=3; s.dmg=Math.max(s.dmg,shock.dmg); }
            showFX(target.id,'debuff'); writeLog(`\\u26A1 Kafka: ${target.name} kena Shock DoT!`,'player-atk');
        }
        if (action==='ultimate') { state.enemies.filter(e=>e.hp>0).forEach(e=>{ applyDmgToEnemy(e,Math.floor(dmg*0.5)); }); }
    } else if (id==='blackswan') {
        dmg=calcDmg(member.atk,180,member.resPen,member.buffAtk);
        if (target) {
            target.statuses=target.statuses||[];
            let arcana=target.statuses.find(s=>s.name==='Arcana');
            if (!arcana) { arcana={name:'Arcana',type:'dot',icon:'\\uD83C\\uDCCF',duration:4,dmg:Math.floor(member.atk*0.8),stacks:1}; target.statuses.push(arcana); }
            else { arcana.stacks=Math.min(7,(arcana.stacks||1)+1); arcana.dmg=Math.floor(member.atk*0.8*arcana.stacks); }
            showFX(target.id,'debuff'); writeLog(`\\uD83C\\uDCCF Black Swan: Arcana x${arcana.stacks} ke ${target.name}!`,'player-atk');
        }
    } else if (id==='silverwolf') {
        if (target) {
            dmg=calcDmg(member.atk, action==='ultimate'?350:130, member.resPen, member.buffAtk);
            if (action==='skill'||action==='ultimate') {
                target.statuses=target.statuses||[];
                target.statuses.push({name:'DEF Shred',type:'weakness',icon:'\\uD83D\\uDD79\\uFE0F',duration:3,defShred:0.4});
                showFX(target.id,'debuff'); writeLog(`\\uD83D\\uDD79\\uFE0F Silver Wolf: DEF Shred -40% ke ${target.name}!`,'player-atk');
            }
        }
    } else if (id==='acheron') {
        dmg=calcDmg(member.atk, action==='ultimate'?450:150, member.resPen, member.buffAtk);
        if (action==='ultimate') { state.enemies.filter(e=>e.hp>0).forEach(e=>{ applyDmgToEnemy(e,Math.floor(dmg*0.5)); }); writeLog('\\uD83D\\uDDE1\\uFE0F Acheron Ult: Abaikan DEF! AoE NUKE!','player-atk'); dmg=0; }
    } else if (id==='jiaoqiu') {
        if (target) {
            dmg=calcDmg(member.atk, action==='ultimate'?300:120, member.resPen, member.buffAtk);
            target.statuses=target.statuses||[];
            target.statuses.push({name:'Ashen Roast',type:'weakness',icon:'\\uD83C\\uDF51',duration:3,defShred:0.4});
            if (action==='ultimate') {
                state.enemies.filter(e=>e.hp>0).forEach(e=>{ e.statuses=e.statuses||[]; e.statuses.push({name:'Hellscape',type:'weakness',icon:'\\uD83D\\uDD25',duration:3,defShred:0.3}); showFX(e.id,'debuff'); });
                writeLog('\\uD83C\\uDF51 Jiaoqiu Ult: Hellscape! Semua musuh lemah!','player-atk');
            } else { showFX(target.id,'debuff'); writeLog(`\\uD83C\\uDF51 Jiaoqiu: Ashen Roast ke ${target.name}!`,'player-atk'); }
        }
    } else if (id==='blade') {
        if (action==='skill') {
            let selfDmg=Math.floor(member.maxHp*0.1); member.hp=Math.max(1,member.hp-selfDmg);
            dmg=calcDmg(member.atk,260,member.resPen,member.buffAtk);
            writeLog(`\\uD83E\\uDE78 Blade Skill: Self -${selfDmg} HP, deal ${dmg} DMG!`,'player-atk');
        } else if (action==='ultimate') {
            let lostHp=member.maxHp-member.hp; let healAmt=Math.floor(lostHp*0.3+member.atk);
            healAlly(member,healAmt); dmg=calcDmg(member.atk,350,member.resPen,member.buffAtk);
            state.enemies.filter(e=>e.hp>0).forEach(e=>applyDmgToEnemy(e,Math.floor(dmg*0.6)));
            dmg=0;
        } else { dmg=calcDmg(member.atk,130,member.resPen,member.buffAtk); }
    } else if (id==='seele') {
        dmg=calcDmg(member.atk, action==='ultimate'?450:150, member.resPen, member.buffAtk);
        if (target && target.hp-dmg<=0 && action!=='ultimate') {
            // Extra turn for Seele on kill
            writeLog('\\uD83E\\uDD8B Seele: Extra Turn setelah Kill!','system');
            if (target) target.hp=Math.max(0,target.hp-dmg);
            renderBattle();
            await sleep(400);
            member.energy=Math.min(member.maxEnergy,member.energy+(eLvl>=4?15:0));
            state.avQueue.unshift({...state.currentActor, av:0});
        }
    } else if (id==='feixiao') {
        dmg=calcDmg(member.atk, action==='ultimate'?480:150, member.resPen, member.buffAtk);
        if (action==='ultimate') {
            state.enemies.filter(e=>e.hp>0).forEach(e=>applyDmgToEnemy(e,Math.floor(dmg*0.4)));
            dmg=0; writeLog('\\uD83D\\uDCA8 Feixiao Ult: Sky-Piercing Nuke!','player-atk');
        }
    } else if (id==='boothill') {
        dmg=calcDmg(member.atk, action==='ultimate'?420:160, member.resPen, member.buffAtk);
        if (target && (action==='skill'||action==='ultimate')) {
            target.statuses=target.statuses||[];
            target.statuses.push({name:'Branded',type:'weakness',icon:'\\uD83E\\uDD20',duration:2,dmg:Math.floor(member.atk*0.5)});
            showFX(target.id,'debuff'); writeLog(`\\uD83E\\uDD20 Boothill: Branded ${target.name}!`,'player-atk');
        }
    } else if (id==='rappa') {
        dmg=calcDmg(member.atk, action==='ultimate'?300:120, member.resPen, member.buffAtk);
        if (action==='ultimate') {
            state.enemies.filter(e=>e.hp>0).forEach(e=>{ applyDmgToEnemy(e,Math.floor(dmg*0.7)); showFX(e.id,'debuff'); e.statuses=e.statuses||[]; e.statuses.push({name:'Ninjutsu',type:'dot',icon:'\\uD83D\\uDCA5',duration:2,dmg:Math.floor(member.atk*0.4)}); });
            dmg=0; writeLog('\\uD83D\\uDCA5 Rappa Ult: Ninjutsu Mode! AoE Break!','player-atk');
        }
    } else if (id==='moze') {
        dmg=calcDmg(member.atk, action==='ultimate'?300:120, member.resPen, member.buffAtk);
        if (target && action==='skill') {
            target.statuses=target.statuses||[];
            target.statuses.push({name:'Marked',type:'weakness',icon:'\\uD83E\\uDFF9',duration:3,dmg:Math.floor(member.atk*0.3)});
            showFX(target.id,'debuff'); writeLog(`\\uD83E\\uDFF9 Moze: ${target.name} Marked! FUA aktif!`,'player-atk');
        }
    } else if (id==='mc') {
        let path = activeMcPath;
        if (path==='physical') { dmg=calcDmg(member.atk, action==='ultimate'?300:action==='skill'?130:100, member.resPen, member.buffAtk); if(action==='ultimate'){state.enemies.filter(e=>e.hp>0).forEach(e=>applyDmgToEnemy(e,Math.floor(dmg*0.5)));dmg=0;} }
        else if (path==='fire') {
            if (action==='skill') { let shAmt=Math.floor(member.atk*0.8+1400); state.party.filter(p=>p.hp>0).forEach(p=>shieldAlly(p,Math.floor(shAmt/state.party.length))); writeLog('\\uD83D\\uDEE1 Azriel Preservation: AoE Shield!','player-atk'); }
            else if (action==='ultimate') { let shAmt=Math.floor(member.atk*1.5+1800); state.party.filter(p=>p.hp>0).forEach(p=>shieldAlly(p,shAmt)); writeLog('\\uD83D\\uDEE1 Azriel Preservation Ult: Party Shield MAX!','player-atk'); }
            else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
        } else if (path==='imaginary') {
            if (action==='skill') { state.party.filter(p=>p.hp>0).forEach(p=>{p.buffAtk=(p.buffAtk||0)+0.5;}); writeLog('\\u2B50 Azriel Harmony Skill: Super Break Buff +50% tim!','player-atk'); state.party.filter(p=>p.hp>0).forEach(p=>showFX(p.id,'buff')); }
            else if (action==='ultimate') { state.enemies.filter(e=>e.hp>0).forEach(e=>applyDmgToEnemy(e,calcDmg(member.atk,200,member.resPen,member.buffAtk))); writeLog('\\u2B50 Azriel Harmony Ult: AoE Imaginary DMG!','player-atk'); }
            else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
        } else { // remembrance
            if (action==='skill') { 
                if(!state.avQueue.find(x=>x.id==='mem')) {
                    state.avQueue.push({id:'mem', av:state.currentActor.av + Math.floor(10000/90), isSummon:true, isPlayer:true});
                    state.memEnergy=0;
                    writeLog(`\\u2744\\uFE0F Azriel: Summon Mem ke medan pertempuran!`,'player-atk');
                } else {
                    state.memEnergy=Math.min(100, (state.memEnergy||0)+30);
                    writeLog(`\\u2744\\uFE0F Azriel Skill: Memulihkan +30 Energi Mem!`,'player-atk');
                }
            }
            else if (action==='ultimate') { 
                let iceDmg=calcDmg(member.atk,250,member.resPen,member.buffAtk); 
                state.enemies.filter(e=>e.hp>0).forEach(e=>{applyDmgToEnemy(e,iceDmg); e.statuses=e.statuses||[]; e.statuses.push({name:'Frozen',type:'weakness',icon:'\\u2744',duration:1,defShred:0.2});}); 
                state.memEnergy=Math.min(100, (state.memEnergy||0)+50);
                writeLog(`\\u2744\\uFE0F Azriel Remembrance Ult: Ice AoE & +50 Energi Mem!`,'player-atk'); 
            }
            else { dmg=calcDmg(member.atk,100,member.resPen,member.buffAtk); }
        }
    } else {
        // Default generic action
        dmg=calcDmg(member.atk, action==='ultimate'?320:action==='skill'?160:100, member.resPen, member.buffAtk);
    }

    // Apply dmg to target
    if (dmg>0 && target) {
        // Apply DEF shred from target statuses
        let shredBonus = (target.statuses||[]).reduce((acc,s)=>acc+(s.defShred||0),0);
        let finalDmg = Math.floor(dmg*(1+shredBonus));
        applyDmgToEnemy(target, finalDmg);
        writeLog(`${member.name} ${action}: -${finalDmg} DMG ke ${target.name}`, 'player-atk');
        if (target.hp<=0) {
            writeLog(`\\u2620 ${target.name} dikalahkan!`, 'system');
            // Check if all enemies dead
            if (state.enemies.every(e=>e.hp<=0)) { await sleep(500); endGame(true); return; }
            // Re-target
            let nextTarget = state.enemies.find(e=>e.hp>0);
            if (nextTarget) state.targetedEnemyId=nextTarget.id;
        }
    }

    renderBattle();
    await sleep(300);
    // Check all enemies dead
    if (state.enemies.every(e=>e.hp<=0)) { endGame(true); return; }
    // Check all allies dead
    if (state.party.every(p=>p.hp<=0)) { endGame(false); return; }
    finishTurn();
};

function finishTurn() {
    let actor = state.avQueue.shift();
    if (actor) {
        // Requeue actor after turn
        if (actor.isSummon) {
            let spd = actor.id==='mem'?90:actor.id==='ll'?60:actor.id==='fuyuan'?90:actor.id==='numby'?80:actor.id==='garmentmaker'?90:90;
            state.avQueue.push({...actor, av:Math.floor(10000/spd)});
        } else {
            let ent = actor.isPlayer ? state.party.find(p=>p.id===actor.id&&p.hp>0) : state.enemies.find(e=>e.id===actor.id&&e.hp>0);
            if (ent) {
                let spd = ent.spd||100;
                state.avQueue.push({...actor, av:Math.floor(10000/spd)});
            }
        }
    }
    state.avQueue.sort((a,b)=>a.av-b.av);
    state.currentActor=null;
    renderBattle(); renderActionOrderBar();
    setTimeout(advanceTurn, 400);
}

async function endGame(isWin) {
    if(isWin) playSFX("win");
    state.waitingForPlayer=false;
    if (state.gameMode === 'su') {
        if (!isWin) {
            writeLog('\\uD83D\\uDC80 KALAH! Perjalanan SU berakhir.', 'system');
            state.stellarJade += 100;
            await saveUserData();
            await sleep(1500);
            playBGM('menu'); navigateTo('main-menu-view');
            return;
        }
        
        state.suStage++;
        if (state.suStage > 5) {
            writeLog('\\uD83C\\uDFC6 SIMULATED UNIVERSE CLEARED! +5000 \\u{1F48E}', 'system');
            state.stellarJade += 5000;
            await saveUserData();
            await sleep(1500);
            playBGM('menu'); navigateTo('main-menu-view');
            return;
        }
        
        state.suPartyHp = {};
        state.party.forEach(p => { state.suPartyHp[p.id] = { hp: p.hp, energy: p.energy }; });
        showSUBuffSelection();
        return;
    }
    let reward = isWin
        ? (state.gameMode==='casual' ? getStageReward(getStageType(state.currentStage)) : 600)
        : (state.gameMode==='casual' ? 30 : 100);
    state.stellarJade += reward;
    if (isWin && state.gameMode==='casual') {
        state.currentStage++;\n        if(state.gameMode==="casual") state.highestCasualStage = Math.max(state.highestCasualStage||0, state.currentStage);
        writeLog(`\\uD83C\\uDFC6 MENANG! +${reward} \\u{1F48E}. Lanjut ke Stage ${state.currentStage}!`, 'system');
    } else {
        writeLog(`${isWin?'\\uD83C\\uDFC6 MENANG':'\\uD83D\\uDC80 KALAH'}! +${reward} \\u{1F48E}`, 'system');
    }
    
    // Mission Progress
    if (state.dailyMissions) {
        if (state.gameMode === 'casual') state.dailyMissions.progress.playCasual = (state.dailyMissions.progress.playCasual||0)+1;
        if (isWin) state.dailyMissions.progress.winBattle = (state.dailyMissions.progress.winBattle||0)+1;
    }
    await saveUserData();
    await new Promise(r=>setTimeout(r,1500));
    if (state.gameMode==='casual') { renderCasualView(); playBGM('menu'); navigateTo('casual-view'); }
    else { playBGM('menu'); navigateTo('main-menu-view'); }
}

window.fleeBattle = async () => {
    state.stellarJade = Math.max(0, state.stellarJade+50);
    writeLog('\\u{1F3C3} Melarikan diri! +50 \\u{1F48E}','system');
    await saveUserData();
    await new Promise(r=>setTimeout(r,600));
    if (state.gameMode==='casual') { playBGM('menu'); navigateTo('casual-view'); }
    else { playBGM('menu'); navigateTo('main-menu-view'); }
};
</script>
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML_HEAD + '\n<script type="module">\n' + '</script>\n' )

# Write in parts properly
content = HTML_HEAD + JS_PART1 + JS_PART2 + JS_PART3 + JS_PART4 + JS_PART5

with open(OUT, 'w', encoding='utf-8', errors='replace') as f:
    f.write(content)

lines = content.count('\n')
byt = len(content.encode('utf-8','replace'))
print(f"Done! Lines: {lines}, Bytes: {byt}")

# Quick verify
checks = ['getMcEidolonKey','feixiao','boothill','yunli','jiaoqiu','sunday','fugue','rappa','gallagher','lingsha','moze','1220','1315','1221','1218','1313','1317','1301','1222','1223','setMcPath','advanceTurn','endGame','renderCasualView','suggestTeam']
for c in checks:
    ok = c in content
    if not ok: print(f'MISSING: {c}')
print('All checks passed!' if all(c in content for c in checks) else 'Some checks failed!')
