/* The Complete C Programming Course — page behaviour (no dependencies) */
(function () {
  "use strict";
  var root = window.SITE_ROOT || "";
  var doc = document;

  /* ---------- theme ---------- */
  var themeBtn = doc.getElementById("theme");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = doc.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      doc.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) { /* storage may be blocked */ }
    });
  }

  /* ---------- mobile menu ---------- */
  var menu = doc.getElementById("menu"), sidebar = doc.getElementById("sidebar"), scrim = doc.getElementById("scrim");
  function setMenu(open) {
    if (!sidebar) return;
    sidebar.classList.toggle("open", open);
    if (scrim) scrim.classList.toggle("show", open);
    if (menu) menu.setAttribute("aria-expanded", open ? "true" : "false");
  }
  if (menu) menu.addEventListener("click", function () { setMenu(!sidebar.classList.contains("open")); });
  if (scrim) scrim.addEventListener("click", function () { setMenu(false); });
  doc.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* keep the current chapter visible in the sidebar */
  var active = doc.querySelector(".sidebar .active");
  if (active && sidebar) {
    try { sidebar.scrollTop = Math.max(0, active.offsetTop - sidebar.clientHeight / 3); } catch (e) { /* ignore */ }
  }

  /* ---------- copy buttons ---------- */
  doc.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest(".copy") : null;
    if (!btn) return;
    var code = btn.parentNode.querySelector("code");
    if (!code) return;
    var text = code.innerText.replace(/\n$/, "");
    function done() { btn.textContent = "Copied!"; setTimeout(function () { btn.textContent = "Copy"; }, 1600); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, fallback);
    } else { fallback(); }
    function fallback() {
      try {
        var ta = doc.createElement("textarea");
        ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
        doc.body.appendChild(ta); ta.select(); doc.execCommand("copy"); doc.body.removeChild(ta); done();
      } catch (err) { btn.textContent = "Press Ctrl+C"; }
    }
  });

  /* ---------- "on this page" highlighting ---------- */
  var tocLinks = [].slice.call(doc.querySelectorAll(".toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var heads = [].slice.call(doc.querySelectorAll("article h2[id], article h3[id]"));
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting && map[en.target.id]) {
          tocLinks.forEach(function (a) { a.classList.remove("on"); });
          map[en.target.id].classList.add("on");
        }
      });
    }, { rootMargin: "-70px 0px -70% 0px" });
    heads.forEach(function (h) { io.observe(h); });
  }

  /* ---------- search ---------- */
  var input = doc.getElementById("q"), box = doc.getElementById("results");
  if (!input || !box) return;
  if (window.matchMedia && matchMedia("(max-width: 600px)").matches) input.placeholder = "Search, or jump to Ex 5.67";
  var index = null, loading = null, hits = [], sel = -1;
  var KIND = { lesson: "Lesson", solution: "Solution", appendix: "Appendix", home: "Home" };

  function load() {
    if (index) return Promise.resolve(index);
    if (!loading) {
      loading = fetch(root + "assets/search.json").then(function (r) { return r.json(); }).then(function (j) { index = j; return j; });
    }
    return loading;
  }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function find(term) {
    term = term.trim().toLowerCase();
    if (!term) return [];
    var m = term.match(/^(?:ex(?:ercise)?\.?\s*)?(\d+)\.(\d+)$/);
    var out = [];
    if (m) {
      var key = "ex " + m[1] + "." + m[2] + " ";
      index.forEach(function (e) { if ((e[0].toLowerCase() + " ").indexOf(key) === 0) out.push(e); });
      out.sort(function (a, b) { return (a[2] === "lesson" ? 0 : 1) - (b[2] === "lesson" ? 0 : 1); });
      return out.slice(0, 10);
    }
    var words = term.split(/\s+/);
    index.forEach(function (e) {
      var t = e[0].toLowerCase(), ok = true, score = 0;
      for (var i = 0; i < words.length; i++) {
        var p = t.indexOf(words[i]);
        if (p < 0) { ok = false; break; }
        score += p;
      }
      if (ok) out.push([e, score + (e[2] === "solution" ? 40 : 0) + (e[0].indexOf("Ex ") === 0 ? 25 : 0)]);
    });
    out.sort(function (a, b) { return a[1] - b[1]; });
    return out.slice(0, 12).map(function (x) { return x[0]; });
  }

  function render() {
    if (!hits.length) {
      box.innerHTML = input.value.trim() ? '<div class="none">No matches. Try another word, or an exercise number like <b>5.67</b>.</div>' : "";
      box.hidden = !input.value.trim();
      return;
    }
    box.innerHTML = hits.map(function (e, i) {
      return '<a href="' + root + e[1] + '" data-i="' + i + '" class="' + (i === sel ? "sel" : "") + '"><span class="kind">' +
        (KIND[e[2]] || "") + "</span><span>" + esc(e[0]) + "</span></a>";
    }).join("");
    box.hidden = false;
  }

  input.addEventListener("input", function () {
    load().then(function () { hits = find(input.value); sel = hits.length ? 0 : -1; render(); });
  });
  input.addEventListener("focus", function () { load(); if (input.value.trim()) { hits = find(input.value); render(); } });
  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown" && hits.length) { sel = (sel + 1) % hits.length; render(); e.preventDefault(); }
    else if (e.key === "ArrowUp" && hits.length) { sel = (sel - 1 + hits.length) % hits.length; render(); e.preventDefault(); }
    else if (e.key === "Enter" && hits[sel]) { window.location.href = root + hits[sel][1]; }
    else if (e.key === "Escape") { box.hidden = true; input.blur(); }
  });
  doc.addEventListener("click", function (e) { if (!e.target.closest || !e.target.closest(".search")) box.hidden = true; });
  doc.addEventListener("keydown", function (e) {
    if (e.key === "/" && doc.activeElement !== input && !/INPUT|TEXTAREA/.test(doc.activeElement.tagName)) { input.focus(); e.preventDefault(); }
  });
})();
