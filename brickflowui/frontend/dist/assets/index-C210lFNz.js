import { j as jsxRuntimeExports, R as React, r as reactExports, a as ReactDOM } from "./vendor-D_MD1exS.js";
import { R as ResponsiveContainer, T as Treemap, F as FunnelChart, a as Tooltip, b as Funnel, C as Cell, c as RadarChart, P as PolarGrid, d as PolarAngleAxis, e as PolarRadiusAxis, L as Legend, f as Radar, g as ComposedChart, h as CartesianGrid, X as XAxis, Y as YAxis, A as Area, B as Bar, i as Line, S as ScatterChart, j as Scatter, k as PieChart, l as Pie, m as BarChart, n as LineChart, o as AreaChart } from "./charts-CbObG0ND.js";
(function polyfill() {
  const relList = document.createElement("link").relList;
  if (relList && relList.supports && relList.supports("modulepreload")) return;
  for (const link of document.querySelectorAll('link[rel="modulepreload"]')) processPreload(link);
  new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type !== "childList") continue;
      for (const node of mutation.addedNodes) if (node.tagName === "LINK" && node.rel === "modulepreload") processPreload(node);
    }
  }).observe(document, {
    childList: true,
    subtree: true
  });
  function getFetchOpts(link) {
    const fetchOpts = {};
    if (link.integrity) fetchOpts.integrity = link.integrity;
    if (link.referrerPolicy) fetchOpts.referrerPolicy = link.referrerPolicy;
    if (link.crossOrigin === "use-credentials") fetchOpts.credentials = "include";
    else if (link.crossOrigin === "anonymous") fetchOpts.credentials = "omit";
    else fetchOpts.credentials = "same-origin";
    return fetchOpts;
  }
  function processPreload(link) {
    if (link.ep) return;
    link.ep = true;
    const fetchOpts = getFetchOpts(link);
    fetch(link.href, fetchOpts);
  }
})();
const LUCIDE_ICON_MAP = {
  Home: "M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z M9 22V12h6v10",
  Database: "M12 2C6.48 2 2 4.24 2 7s4.48 5 10 5 10-2.24 10-5S17.52 2 12 2zM2 17c0 2.76 4.48 5 10 5s10-2.24 10-5M2 12c0 2.76 4.48 5 10 5s10-2.24 10-5",
  LayoutDashboard: "M3 3h7v7H3zM14 3h7v7h-7zM14 14h7v7h-7zM3 14h7v7H3z",
  GitBranch: "M6 3v12M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM18 9a9 9 0 0 1-9 9",
  FlaskConical: "M14 2v6l3 10H7L10 8V2M8.5 2h7",
  Settings: "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z",
  Lock: "M19 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2zM7 11V7a5 5 0 0 1 10 0v4",
  Hash: "M4 9h16M4 15h16M10 3L8 21M16 3l-2 18",
  Activity: "M22 12h-4l-3 9L9 3l-3 9H2",
  Clock: "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 6v6l4 2",
  Server: "M2 3h20v6H2zM2 15h20v6H2zM6 9v6M18 9v6",
  AlertTriangle: "M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01",
  CheckCircle: "M22 11.08V12a10 10 0 1 1-5.93-9.14M22 4L12 14.01l-3-3",
  XCircle: "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM15 9l-6 6M9 9l6 6",
  PlayCircle: "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM10 8l6 4-6 4V8z",
  Target: "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12zM12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM22 12h-2M2 12h2M12 2v2M12 22v-2",
  Sparkles: "M12 3l1.8 4.2L18 9l-4.2 1.8L12 15l-1.8-4.2L6 9l4.2-1.8L12 3zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9L19 15zM5 15l.9 2.1L8 18l-2.1.9L5 21l-.9-2.1L2 18l2.1-.9L5 15z",
  Inbox: "M4 4h16v10l-3 4H7l-3-4V4zM4 14h4l2 3h4l2-3h4",
  X: "M18 6L6 18M6 6l12 12"
};
const CHART_COLORS = ["#FF3621", "#58a6ff", "#3fb950", "#e3b341", "#bc8cff", "#d28c3c"];
function Icon({ name, size = 16 }) {
  const path = LUCIDE_ICON_MAP[name];
  if (!path) return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { style: { fontSize: size - 2, opacity: 0.6 }, children: "◆" });
  return /* @__PURE__ */ jsxRuntimeExports.jsx(
    "svg",
    {
      xmlns: "http://www.w3.org/2000/svg",
      width: size,
      height: size,
      viewBox: "0 0 24 24",
      fill: "none",
      stroke: "currentColor",
      strokeWidth: "2",
      strokeLinecap: "round",
      strokeLinejoin: "round",
      children: path.split("M").filter(Boolean).map((d, i) => /* @__PURE__ */ jsxRuntimeExports.jsx("path", { d: "M" + d }, i))
    }
  );
}
function resolveMotionClass(props, base = []) {
  const classes = [...base];
  if (props.animated) classes.push("bf-animated");
  if (props.elevated) classes.push("bf-elevated");
  if (props.loading) classes.push("bf-is-loading");
  if (props.animation) classes.push(`bf-anim-${props.animation}`);
  return classes.filter(Boolean).join(" ");
}
function resolveMotionStyle(props) {
  const style = { ...props.style || {} };
  if (props.animationDelay !== void 0 && props.animationDelay !== null) {
    style.animationDelay = `${props.animationDelay}s`;
  }
  return style;
}
function pendingEventIds(props, keys = ["click", "change", "submit", "close", "rowClick", "nodeClick", "cardClick"]) {
  return keys.map((key) => props[key]).filter((value) => typeof value === "string" && value.length > 0);
}
function isPending(props, ctx, keys) {
  return pendingEventIds(props, keys).some((eventId) => (ctx.pendingEvents.get(eventId) || 0) > 0);
}
function renderLoadingSkeleton(lines = 3) {
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-skeleton-stack", children: Array.from({ length: lines }).map((_, index) => /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-skeleton-line" }, index)) });
}
function chartShell(key, props, content) {
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chart-container bf-chart-enter", children: [
    props.title && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: props.title }),
    content
  ] }, key);
}
function chartState(key, props) {
  if (props.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: renderLoadingSkeleton(4) }, key);
  const data = props.data || [];
  if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: props.emptyMessage || "No chart data available" }, key);
  return null;
}
function statusTone(status) {
  const normalized = String(status || "neutral").toLowerCase();
  if (["success", "healthy", "ok", "running", "passed", "complete", "completed"].includes(normalized)) return "success";
  if (["warning", "watch", "delayed", "queued", "degraded"].includes(normalized)) return "warning";
  if (["error", "failed", "critical", "blocked", "at risk", "atrisk"].includes(normalized)) return "error";
  if (["info", "active", "processing"].includes(normalized)) return "info";
  return "neutral";
}
function Renderer({
  node,
  dispatch,
  navigate,
  pendingEvents,
  themeMode,
  setThemeMode
}) {
  const ctx = { dispatch, navigate, pendingEvents, themeMode, setThemeMode };
  return /* @__PURE__ */ jsxRuntimeExports.jsx(jsxRuntimeExports.Fragment, { children: renderNode(node, ctx, "0") });
}
function renderChildren(children, ctx, prefix) {
  return children.map((child, i) => renderNode(child, ctx, `${prefix}-${i}`));
}
function renderNode(node, ctx, key) {
  if (!node) return null;
  const { type, props, children } = node;
  const p = props;
  const ev = (eventName, arg) => {
    const eventId = p[eventName];
    if (eventId) ctx.dispatch(eventId, arg === void 0 ? {} : { value: arg });
  };
  switch (type) {
    // ── Text ───────────────────────────────────────────────────────────────
    case "Text": {
      const variant = p.variant || "body";
      const cls = ["bf-text-" + variant, p.muted ? "bf-text-muted" : "", p.bold ? "bf-text-bold" : "", p.italic ? "bf-text-italic" : ""].filter(Boolean).join(" ");
      const Tag = { h1: "h1", h2: "h2", h3: "h3", h4: "h4", code: "code", label: "label", caption: "small" }[variant] || "p";
      return React.createElement(Tag, { key, className: cls, style: p.color ? { color: p.color } : void 0 }, p.value);
    }
    case "Code":
      return /* @__PURE__ */ jsxRuntimeExports.jsx("pre", { className: "bf-code-block", children: /* @__PURE__ */ jsxRuntimeExports.jsx("code", { children: p.value }) }, key);
    // ── Layout ─────────────────────────────────────────────────────────────
    case "Column": {
      const pad = (p.padding || 0) * 4;
      const gap = (p.gap || 2) * 4;
      const alignMap = { start: "flex-start", end: "flex-end", center: "center", stretch: "stretch" };
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-column", style: { display: "flex", flexDirection: "column", gap, padding: pad, alignItems: alignMap[p.align] || "stretch", width: "100%", ...p.style || {} }, children: renderChildren(children, ctx, key) }, key);
    }
    case "Row": {
      const gap = (p.gap || 2) * 4;
      const alignMap = { start: "flex-start", end: "flex-end", center: "center", stretch: "stretch" };
      const justifyMap = { start: "flex-start", end: "flex-end", center: "center", between: "space-between", around: "space-around" };
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-row", style: { display: "flex", flexDirection: "row", gap, flexWrap: p.wrap !== false ? "wrap" : "nowrap", alignItems: alignMap[p.align] || "center", justifyContent: justifyMap[p.justify] || "flex-start", width: "100%", ...p.style || {} }, children: renderChildren(children, ctx, key) }, key);
    }
    case "Card": {
      const cls = resolveMotionClass(p, ["bf-card", p.bordered ? "bordered" : "", p.hover ? "hoverable" : ""]);
      const pad = (p.padding || 5) * 4;
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: cls, style: { padding: pad, ...resolveMotionStyle(p) }, children: [
        p.title || p.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-card-header", children: [
          p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-card-title", children: p.title }) : null,
          p.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-card-subtitle", children: p.subtitle }) : null
        ] }) : null,
        renderChildren(children, ctx, key)
      ] }, key);
    }
    case "Grid": {
      const cols = p.cols || 2;
      const gap = (p.gap || 4) * 4;
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-grid", style: { "--cols": cols, gap }, children: renderChildren(children, ctx, key) }, key);
    }
    case "Divider":
      return p.label ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-divider-labeled", children: /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: p.label }) }, key) : /* @__PURE__ */ jsxRuntimeExports.jsx("hr", { className: "bf-divider" }, key);
    case "Spacer":
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { style: { height: (p.size || 4) * 4 } }, key);
    // ── Controls ───────────────────────────────────────────────────────────
    case "Button": {
      const autoLoading = isPending(p, ctx, ["click"]);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs(
        "button",
        {
          className: resolveMotionClass({ ...p, loading: Boolean(p.loading) || autoLoading }, ["bf-btn", `bf-btn-${p.variant || "primary"}`]),
          disabled: p.disabled || p.loading || autoLoading || false,
          type: p.htmlType || "button",
          style: resolveMotionStyle(p),
          onClick: () => ev("click"),
          children: [
            (p.loading || autoLoading) && /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-spinner bf-spinner-sm" }),
            p.icon && /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: p.icon, size: 14 }),
            p.label
          ]
        },
        key
      );
    }
    case "Input":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(InputComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    case "DateRangePicker":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(DateRangePickerComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    case "MultiSelect":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(MultiSelectComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    case "Select":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(SelectComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    case "Checkbox":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(CheckboxComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    case "Toggle": {
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ToggleComponent, { props: p, dispatch: (v) => ev("change", v), pending: isPending(p, ctx, ["change"]) }, key);
    }
    case "Slider":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(SliderComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["change"]) }, dispatch: (value) => ev("change", value) }, key);
    // ── Data display ───────────────────────────────────────────────────────
    case "Breadcrumbs":
      return /* @__PURE__ */ jsxRuntimeExports.jsx("nav", { className: "bf-breadcrumbs", "aria-label": "Breadcrumb", children: (p.items || []).map((item, index, items) => {
        const isLast = index === items.length - 1;
        return /* @__PURE__ */ jsxRuntimeExports.jsxs(React.Fragment, { children: [
          isLast || !item.path ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-breadcrumb-current", children: String(item.label ?? "") }) : /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-breadcrumb-link", onClick: () => ctx.navigate(String(item.path)), children: String(item.label ?? "") }),
          !isLast ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-breadcrumb-sep", children: "/" }) : null
        ] }, `${key}-crumb-${index}`);
      }) }, key);
    case "EmptyState":
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-empty-state"]), style: resolveMotionStyle(p), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-empty-state-icon", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: p.icon || "Inbox", size: 18 }) }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-empty-state-title", children: p.title }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-empty-state-message", children: p.message }),
        p.actions?.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-empty-state-actions", children: renderChildren(p.actions || [], ctx, `${key}-actions`) }) : null
      ] }, key);
    case "Table":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(TableComponent, { props: p, dispatch: ctx.dispatch }, key);
    case "Badge":
      return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: `bf-badge bf-badge-${p.color || "blue"}`, children: p.label }, key);
    case "Alert":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(AlertComponent, { props: p }, key);
    case "Spinner":
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-spinner bf-spinner-${p.size || "md"}` }, key);
    case "Progress": {
      const pct = Math.min(100, p.value / (p.max || 100) * 100);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-progress-wrapper"]), style: resolveMotionStyle(p), children: [
        p.label && /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-progress-label", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: p.label }),
          /* @__PURE__ */ jsxRuntimeExports.jsxs("span", { children: [
            Math.round(pct),
            "%"
          ] })
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-progress-track", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-progress-fill ${p.animated ? "animated" : ""}`, style: { width: `${pct}%`, background: `var(--db-${p.color || "primary"})` } }) })
      ] }, key);
    }
    case "Stat": {
      const deltaType = p.deltaType || "neutral";
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-stat"]), style: resolveMotionStyle(p), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { style: { display: "flex", alignItems: "center", gap: 6 }, children: [
          p.icon && /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: p.icon, size: 16 }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stat-label", children: p.label })
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx(AnimatedValue, { value: p.value, animated: Boolean(p.animated) }),
        p.delta && /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-stat-delta ${deltaType}`, children: [
          deltaType === "increase" ? "▲" : deltaType === "decrease" ? "▼" : "—",
          " ",
          p.delta
        ] })
      ] }, key);
    }
    // ── Navigation ──────────────────────────────────────────────────────────
    case "Sidebar":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(SidebarComponent, { props: p, children, ctx }, key);
    case "TopNav":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(TopNavComponent, { props: p, children, ctx }, key);
    // NavItem is rendered as part of Sidebar above; standalone fallback:
    case "NavItem":
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { className: "bf-nav-item", onClick: () => ctx.navigate(p.path), children: [
        p.icon && /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: p.icon, size: 16 }),
        p.label
      ] }, key);
    // ── Tabs ───────────────────────────────────────────────────────────────
    case "Tabs":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(TabsComponent, { props: p, children, ctx, nodeKey: key, dispatch: ctx.dispatch }, key);
    case "TabItem":
      return null;
    // Rendered inside Tabs
    // ── Modal ──────────────────────────────────────────────────────────────
    case "Accordion":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(AccordionComponent, { props: p, children, ctx, nodeKey: key }, key);
    case "AccordionItem":
      return null;
    case "Modal":
      if (!p.visible) return null;
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-modal-overlay", onClick: () => ev("close"), children: /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, [`bf-modal`, `bf-modal-${p.size || "md"}`]), style: resolveMotionStyle(p), onClick: (e) => e.stopPropagation(), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-modal-header", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-modal-title", children: p.title }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-modal-close", onClick: () => ev("close"), children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 16 }) })
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-modal-body", children: renderChildren(children, ctx, key) })
      ] }) }, key);
    // ── Form ───────────────────────────────────────────────────────────────
    case "Drawer":
      if (!p.visible) return null;
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-drawer-overlay", onClick: () => ev("close"), children: /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, [`bf-drawer`, `bf-drawer-${p.side || "right"}`]), style: { width: p.width || "420px", ...resolveMotionStyle(p) }, onClick: (e) => e.stopPropagation(), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-drawer-header", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-drawer-title", children: p.title }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-modal-close", onClick: () => ev("close"), children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 16 }) })
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-drawer-body", children: renderChildren(children, ctx, key) })
      ] }) }, key);
    case "Popup":
      if (!p.visible) return null;
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-popup-shell bf-popup-${p.placement || "center"}`, children: [
        Boolean(p.backdrop) ? /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-popup-backdrop", onClick: () => ev("close"), "aria-label": "Close popup" }) : null,
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, [`bf-popup`, `bf-popup-${p.size || "sm"}`]), style: resolveMotionStyle(p), onClick: (e) => e.stopPropagation(), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-popup-header", children: [
            /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-popup-title", children: p.title }),
            /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-modal-close", onClick: () => ev("close"), children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 16 }) })
          ] }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-popup-body", children: renderChildren(children, ctx, key) })
        ] })
      ] }, key);
    case "Form":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(FormComponent, { props: p, children, ctx, nodeKey: key }, key);
    // ── Charts ─────────────────────────────────────────────────────────────
    case "AreaChart": {
      const yKeys = p.yKeys || [];
      const data = p.data || [];
      if (p.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: renderLoadingSkeleton(4) }, key);
      if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No chart data available" }, key);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chart-container", children: [
        p.title && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: p.title }),
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(AreaChart, { data, onClick: (state) => p.click && ev("click", state?.activePayload?.[0]?.payload ?? {}), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("defs", { children: yKeys.map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsxs("linearGradient", { id: `agrad-${i}`, x1: "0", y1: "0", x2: "0", y2: "1", children: [
            /* @__PURE__ */ jsxRuntimeExports.jsx("stop", { offset: "5%", stopColor: p.colors?.[i] || CHART_COLORS[i % CHART_COLORS.length], stopOpacity: 0.25 }),
            /* @__PURE__ */ jsxRuntimeExports.jsx("stop", { offset: "95%", stopColor: p.colors?.[i] || CHART_COLORS[i % CHART_COLORS.length], stopOpacity: 0 })
          ] }, yk)) }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(CartesianGrid, { strokeDasharray: "3 3" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(XAxis, { dataKey: p.xKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(YAxis, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          yKeys.map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Area, { type: "monotone", dataKey: yk, stroke: p.colors?.[i] || CHART_COLORS[i % CHART_COLORS.length], fill: `url(#agrad-${i})`, strokeWidth: 2 }, yk))
        ] }) })
      ] }, key);
    }
    case "LineChart": {
      const yKeys = p.yKeys || [];
      const data = p.data || [];
      if (p.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: renderLoadingSkeleton(4) }, key);
      if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No chart data available" }, key);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chart-container", children: [
        p.title && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: p.title }),
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(LineChart, { data, onClick: (state) => p.click && ev("click", state?.activePayload?.[0]?.payload ?? {}), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(CartesianGrid, { strokeDasharray: "3 3" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(XAxis, { dataKey: p.xKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(YAxis, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Legend, {}),
          yKeys.map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Line, { type: "monotone", dataKey: yk, stroke: CHART_COLORS[i % CHART_COLORS.length], strokeWidth: 2, dot: false }, yk))
        ] }) })
      ] }, key);
    }
    case "BarChart": {
      const yKeys = p.yKeys || [];
      const data = p.data || [];
      if (p.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: renderLoadingSkeleton(4) }, key);
      if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No chart data available" }, key);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chart-container", children: [
        p.title && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: p.title }),
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(BarChart, { data, layout: p.horizontal ? "vertical" : "horizontal", onClick: (state) => p.click && ev("click", state?.activePayload?.[0]?.payload ?? {}), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(CartesianGrid, { strokeDasharray: "3 3" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(XAxis, { dataKey: p.horizontal ? void 0 : p.xKey, type: p.horizontal ? "number" : "category" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(YAxis, { dataKey: p.horizontal ? p.xKey : void 0, type: p.horizontal ? "category" : "number" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          yKeys.map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Bar, { dataKey: yk, fill: CHART_COLORS[i % CHART_COLORS.length], radius: [3, 3, 0, 0] }, yk))
        ] }) })
      ] }, key);
    }
    case "DonutChart": {
      const data = p.data || [];
      const vk = p.valueKey || "value";
      const lk = p.labelKey || "label";
      if (p.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: renderLoadingSkeleton(4) }, key);
      if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No chart data available" }, key);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chart-container", children: [
        p.title && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: p.title }),
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(PieChart, { children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(Pie, { data, cx: "50%", cy: "50%", innerRadius: "55%", outerRadius: "75%", dataKey: vk, nameKey: lk, paddingAngle: 2, onClick: (payload) => p.click && ev("click", payload?.payload ?? {}), children: data.map((_, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Cell, { fill: (p.colors || [])[i] || CHART_COLORS[i % CHART_COLORS.length] }, i)) }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, { formatter: (value, name) => [value, name] }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Legend, {})
        ] }) })
      ] }, key);
    }
    case "ScatterChart": {
      const state = chartState(key, p);
      if (state) return state;
      return chartShell(
        key,
        p,
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(ScatterChart, { data: p.data || [], onClick: (state2) => p.click && ev("click", state2?.activePayload?.[0]?.payload ?? {}), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(CartesianGrid, { strokeDasharray: "3 3" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(XAxis, { dataKey: p.xKey, type: "number", name: p.xKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(YAxis, { dataKey: p.yKey, type: "number", name: p.yKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, { cursor: { strokeDasharray: "3 3" } }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Scatter, { dataKey: p.yKey, fill: p.color || CHART_COLORS[0] })
        ] }) })
      );
    }
    case "ComposedChart": {
      const state = chartState(key, p);
      if (state) return state;
      const colors = p.colors || CHART_COLORS;
      return chartShell(
        key,
        p,
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 320, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(ComposedChart, { data: p.data || [], onClick: (state2) => p.click && ev("click", state2?.activePayload?.[0]?.payload ?? {}), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(CartesianGrid, { strokeDasharray: "3 3" }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(XAxis, { dataKey: p.xKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(YAxis, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Legend, {}),
          (p.areaKeys || []).map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Area, { type: "monotone", dataKey: yk, fill: colors[i % colors.length], stroke: colors[i % colors.length], fillOpacity: 0.18 }, `area-${yk}`)),
          (p.barKeys || []).map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Bar, { dataKey: yk, fill: colors[(i + 2) % colors.length], radius: [3, 3, 0, 0] }, `bar-${yk}`)),
          (p.lineKeys || []).map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Line, { type: "monotone", dataKey: yk, stroke: colors[(i + 4) % colors.length], strokeWidth: 2, dot: false }, `line-${yk}`))
        ] }) })
      );
    }
    case "GaugeChart":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(GaugeChartComponent, { props: p }, key);
    case "RadarChart": {
      const state = chartState(key, p);
      if (state) return state;
      const colors = p.colors || CHART_COLORS;
      return chartShell(
        key,
        p,
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 320, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(RadarChart, { data: p.data || [], children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(PolarGrid, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(PolarAngleAxis, { dataKey: p.angleKey }),
          /* @__PURE__ */ jsxRuntimeExports.jsx(PolarRadiusAxis, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Legend, {}),
          (p.valueKeys || []).map((yk, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Radar, { name: yk, dataKey: yk, stroke: colors[i % colors.length], fill: colors[i % colors.length], fillOpacity: 0.18 }, yk))
        ] }) })
      );
    }
    case "Heatmap":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(HeatmapComponent, { props: p, dispatch: (value) => ev("click", value) }, key);
    case "FunnelChart": {
      const state = chartState(key, p);
      if (state) return state;
      const data = p.data || [];
      return chartShell(
        key,
        p,
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsxs(FunnelChart, { children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx(Tooltip, {}),
          /* @__PURE__ */ jsxRuntimeExports.jsx(Funnel, { dataKey: p.valueKey || "value", nameKey: p.labelKey || "label", data, isAnimationActive: true, onClick: (payload) => p.click && ev("click", payload?.payload ?? {}), children: data.map((_, i) => /* @__PURE__ */ jsxRuntimeExports.jsx(Cell, { fill: (p.colors || [])[i] || CHART_COLORS[i % CHART_COLORS.length] }, i)) })
        ] }) })
      );
    }
    case "TreeMap": {
      const state = chartState(key, p);
      if (state) return state;
      return chartShell(
        key,
        p,
        /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: p.height || 300, children: /* @__PURE__ */ jsxRuntimeExports.jsx(
          Treemap,
          {
            data: p.data || [],
            dataKey: p.valueKey || "value",
            nameKey: p.nameKey || "name",
            stroke: "var(--db-surface)",
            fill: (p.colors || [])[0] || CHART_COLORS[0],
            onClick: (payload) => p.click && ev("click", payload?.payload ?? payload ?? {})
          }
        ) })
      );
    }
    case "PipelineGraph":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(PipelineGraphComponent, { props: p, dispatch: (value) => ev("nodeClick", value) }, key);
    case "Hero":
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("section", { className: resolveMotionClass(p, ["bf-hero"]), style: resolveMotionStyle(p), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-hero-content", children: [
          p.eyebrow ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-hero-eyebrow", children: p.eyebrow }) : null,
          p.image ? /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-hero-brand", children: [
            /* @__PURE__ */ jsxRuntimeExports.jsx("img", { className: "bf-hero-brand-image", src: p.image, alt: p.imageAlt || p.title }),
            p.tagline ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-hero-brand-tagline", children: p.tagline }) : null
          ] }) : p.tagline ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-hero-brand-tagline", children: p.tagline }) : null,
          /* @__PURE__ */ jsxRuntimeExports.jsx("h1", { className: "bf-hero-title", children: p.title }),
          p.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("p", { className: "bf-hero-subtitle", children: p.subtitle }) : null,
          p.badges?.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-hero-badges", children: renderChildren(p.badges || [], ctx, `${key}-badges`) }) : null,
          p.actions?.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-hero-actions", children: renderChildren(p.actions || [], ctx, `${key}-actions`) }) : null
        ] }),
        children.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-hero-visual", children: renderChildren(children, ctx, `${key}-visual`) }) : null
      ] }, key);
    case "SectionHeader":
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-section-header"]), style: resolveMotionStyle(p), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { children: [
          p.eyebrow ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-section-eyebrow", children: p.eyebrow }) : null,
          /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-section-title", children: p.title }),
          p.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-section-subtitle", children: p.subtitle }) : null
        ] }),
        p.actions?.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-section-actions", children: renderChildren(p.actions || [], ctx, `${key}-actions`) }) : null
      ] }, key);
    case "StatusStrip":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(StatusStripComponent, { props: p }, key);
    case "Stepper":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(StepperComponent, { props: p }, key);
    case "KanbanBoard":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(KanbanBoardComponent, { props: p, dispatch: (value) => ev("cardClick", value) }, key);
    case "ChatMessage":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ChatMessageComponent, { props: p }, key);
    case "ChatInput":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ChatInputComponent, { props: { ...p, loading: Boolean(p.loading) || isPending(p, ctx, ["submit", "change"]) }, dispatchChange: (value) => ev("change", value), dispatchSubmit: (value) => ev("submit", value) }, key);
    case "Toast":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ToastComponent, { props: p, dispatchClose: () => ev("close") }, key);
    case "Image":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ImageComponent, { props: p }, key);
    case "Video":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(VideoComponent, { props: p }, key);
    case "Embed":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(EmbedComponent, { props: p }, key);
    case "ThemeToggle":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(ThemeToggleComponent, { props: p, ctx }, key);
    case "Timeline":
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-timeline"]), style: resolveMotionStyle(p), children: [
        p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-card-title", style: { marginBottom: 12 }, children: p.title }) : null,
        (p.items || []).map((item, index) => /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-timeline-item", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-timeline-dot" }),
          /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-timeline-content", children: [
            /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-timeline-row", children: [
              /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-timeline-title", children: String(item.title ?? "") }),
              item.time ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-timeline-time", children: String(item.time) }) : null
            ] }),
            item.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-timeline-subtitle", children: String(item.subtitle) }) : null,
            item.description ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-timeline-description", children: String(item.description) }) : null
          ] })
        ] }, `${key}-timeline-${index}`))
      ] }, key);
    case "SparklineStat":
      return /* @__PURE__ */ jsxRuntimeExports.jsx(SparklineStatComponent, { props: p }, key);
    default:
      return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-node-${type.toLowerCase()}`, children: renderChildren(children, ctx, key) }, key);
  }
}
function ToggleComponent({ props: p, dispatch, pending }) {
  const incomingChecked = Boolean(p.checked);
  const [checked, setChecked] = reactExports.useState(incomingChecked);
  reactExports.useEffect(() => {
    setChecked(incomingChecked);
  }, [incomingChecked]);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs(
    "label",
    {
      className: resolveMotionClass(p, [`bf-toggle-wrapper`, pending ? "is-loading" : ""]),
      style: resolveMotionStyle(p),
      onClick: () => {
        if (!p.disabled && !pending) {
          const next = !checked;
          setChecked(next);
          dispatch(next);
        }
      },
      children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-toggle-switch ${checked ? "checked" : ""}` }),
        p.label,
        pending ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-spinner bf-spinner-sm" }) : null
      ]
    }
  );
}
function CheckboxComponent({ props: p, dispatch }) {
  const incomingChecked = Boolean(p.checked);
  const [checked, setChecked] = reactExports.useState(incomingChecked);
  reactExports.useEffect(() => {
    setChecked(incomingChecked);
  }, [incomingChecked]);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("label", { className: resolveMotionClass(p, ["bf-checkbox-wrapper", p.loading ? "is-loading" : ""]), style: resolveMotionStyle(p), children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx(
      "input",
      {
        type: "checkbox",
        name: p.name,
        checked,
        disabled: Boolean(p.disabled) || Boolean(p.loading),
        onChange: (event) => {
          const next = event.target.checked;
          setChecked(next);
          dispatch(next);
        }
      }
    ),
    p.label,
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-spinner bf-spinner-sm" }) : null
  ] });
}
function SelectComponent({ props: p, dispatch }) {
  const incomingValue = String(p.value || "");
  const [value, setValue] = reactExports.useState(incomingValue);
  reactExports.useEffect(() => {
    setValue(incomingValue);
  }, [incomingValue]);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-form-field"]), style: resolveMotionStyle(p), children: [
    p.label && /* @__PURE__ */ jsxRuntimeExports.jsx("label", { className: "bf-label", children: p.label }),
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-field-loading", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-sm" }) }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsxs(
      "select",
      {
        name: p.name,
        className: "bf-select",
        value,
        disabled: Boolean(p.disabled) || Boolean(p.loading),
        onChange: (event) => {
          const next = event.target.value;
          setValue(next);
          dispatch(next);
        },
        children: [
          p.placeholder ? /* @__PURE__ */ jsxRuntimeExports.jsx("option", { value: "", children: p.placeholder }) : null,
          (p.options || []).map((opt) => /* @__PURE__ */ jsxRuntimeExports.jsx("option", { value: opt.value, children: opt.label }, opt.value))
        ]
      }
    )
  ] });
}
function SliderComponent({ props: p, dispatch }) {
  const incomingValue = Number(p.value ?? 0);
  const [value, setValue] = reactExports.useState(incomingValue);
  reactExports.useEffect(() => {
    setValue(incomingValue);
  }, [incomingValue]);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-slider-wrapper", p.loading ? "bf-is-loading" : ""]), style: resolveMotionStyle(p), children: [
    p.label && /* @__PURE__ */ jsxRuntimeExports.jsx("label", { className: "bf-label", children: p.label }),
    /* @__PURE__ */ jsxRuntimeExports.jsx(
      "input",
      {
        type: "range",
        className: "bf-slider",
        name: p.name,
        min: p.min,
        max: p.max,
        step: p.step,
        value,
        disabled: Boolean(p.disabled) || Boolean(p.loading),
        onChange: (event) => {
          const next = parseFloat(event.target.value);
          setValue(next);
          dispatch(next);
        }
      }
    ),
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-field-loading", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-sm" }) }) : null
  ] });
}
function AlertComponent({ props: p }) {
  const [dismissed, setDismissed] = reactExports.useState(false);
  reactExports.useEffect(() => {
    setDismissed(false);
  }, [p.message, p.title, p.alertType]);
  if (dismissed) return null;
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-alert bf-alert-${p.alertType || "info"}`, children: [
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-alert-body", children: [
      p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-alert-title", children: p.title }) : null,
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { children: p.message })
    ] }),
    Boolean(p.dismissible) ? /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-alert-close", onClick: () => setDismissed(true), "aria-label": "Dismiss alert", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 14 }) }) : null
  ] });
}
function ImageComponent({ props: p }) {
  const variant = p.variant || "content";
  const image = /* @__PURE__ */ jsxRuntimeExports.jsx(
    "img",
    {
      className: `bf-image ${variant === "inline" ? "inline" : ""} ${variant === "avatar" ? "avatar" : ""}`,
      src: p.src,
      alt: p.alt || "",
      loading: p.loadingMode || "lazy",
      style: {
        width: p.width || (variant === "avatar" ? "48px" : "100%"),
        height: p.height || (variant === "avatar" ? p.width || "48px" : "auto"),
        objectFit: p.fit || "cover",
        borderRadius: variant === "avatar" ? "50%" : p.radius || "var(--radius-lg)"
      }
    }
  );
  if (variant === "inline" && !p.caption) {
    return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: resolveMotionClass(p, ["bf-inline-image"]), style: resolveMotionStyle(p), children: image });
  }
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("figure", { className: resolveMotionClass(p, ["bf-image-shell", p.caption ? "has-caption" : ""]), style: resolveMotionStyle(p), children: [
    image,
    p.caption ? /* @__PURE__ */ jsxRuntimeExports.jsx("figcaption", { className: "bf-image-caption", children: p.caption }) : null
  ] });
}
function VideoComponent({ props: p }) {
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("figure", { className: resolveMotionClass(p, ["bf-image-shell", "bf-video-shell", p.caption ? "has-caption" : ""]), style: resolveMotionStyle(p), children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx(
      "video",
      {
        className: "bf-video",
        src: p.src,
        poster: p.poster,
        controls: p.controls !== false,
        autoPlay: Boolean(p.autoplay),
        loop: Boolean(p.loop),
        muted: Boolean(p.muted),
        playsInline: true,
        style: {
          width: p.width || "100%",
          height: p.height || "auto",
          borderRadius: p.radius || "var(--radius-lg)"
        }
      }
    ),
    p.caption ? /* @__PURE__ */ jsxRuntimeExports.jsx("figcaption", { className: "bf-image-caption", children: p.caption }) : null
  ] });
}
function EmbedComponent({ props: p }) {
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: resolveMotionClass(p, ["bf-embed-shell"]), style: resolveMotionStyle(p), children: /* @__PURE__ */ jsxRuntimeExports.jsx(
    "iframe",
    {
      className: "bf-embed-frame",
      src: p.src,
      title: p.title || "Embedded content",
      loading: p.loadingMode || "lazy",
      sandbox: typeof p.sandbox === "string" ? p.sandbox : void 0,
      allowFullScreen: Boolean(p.allowFullscreen),
      style: {
        height: p.height || "420px",
        borderRadius: p.radius || "var(--radius-lg)"
      }
    }
  ) });
}
function ThemeToggleComponent({ props: p, ctx }) {
  const isDark = ctx.themeMode === "dark";
  return /* @__PURE__ */ jsxRuntimeExports.jsxs(
    "button",
    {
      type: "button",
      className: "bf-theme-toggle",
      onClick: () => ctx.setThemeMode(isDark ? "light" : "dark"),
      "aria-label": String(p.label || "Toggle theme"),
      children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-theme-toggle-track", children: /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: `bf-theme-toggle-thumb ${isDark ? "dark" : "light"}` }) }),
        /* @__PURE__ */ jsxRuntimeExports.jsxs("span", { className: "bf-theme-toggle-copy", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("strong", { children: String(p.label || "Theme") }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: isDark ? String(p.darkLabel || "Dark") : String(p.lightLabel || "Light") })
        ] })
      ]
    }
  );
}
function ToastComponent({ props: p, dispatchClose }) {
  const [dismissed, setDismissed] = reactExports.useState(false);
  const close = () => {
    setDismissed(true);
    if (p.close) dispatchClose();
  };
  reactExports.useEffect(() => {
    setDismissed(false);
  }, [p.visible, p.message, p.title, p.alertType]);
  reactExports.useEffect(() => {
    if (!p.autoHideMs || dismissed || p.visible === false) return;
    const timer = window.setTimeout(() => close(), Number(p.autoHideMs));
    return () => window.clearTimeout(timer);
  }, [dismissed, p.autoHideMs, p.visible, p.message, p.title]);
  if (p.visible === false || dismissed) return null;
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, [`bf-toast`, `bf-toast-${p.alertType || "info"}`]), style: resolveMotionStyle(p), children: [
    p.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: p.icon, size: 16 }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-toast-content", children: [
      p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-toast-title", children: p.title }) : null,
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-toast-message", children: p.message })
    ] }),
    p.dismissible !== false ? /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-toast-close", onClick: close, "aria-label": "Dismiss notification", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 14 }) }) : null
  ] });
}
function AnimatedValue({ value, animated }) {
  const parseNumeric = (raw) => {
    const match = raw.match(/-?\d+(?:\.\d+)?/);
    if (!match) return null;
    return {
      number: parseFloat(match[0]),
      prefix: raw.slice(0, match.index ?? 0),
      suffix: raw.slice((match.index ?? 0) + match[0].length),
      decimals: match[0].includes(".") ? match[0].split(".")[1].length : 0
    };
  };
  const parsed = parseNumeric(value);
  const [display, setDisplay] = reactExports.useState(() => {
    if (!animated || !parsed) return value;
    return `${parsed.prefix}${0 .toFixed(parsed.decimals)}${parsed.suffix}`;
  });
  reactExports.useEffect(() => {
    if (!animated || !parsed) {
      setDisplay(value);
      return;
    }
    const duration = 700;
    const start = performance.now();
    let frame = 0;
    const tick = (now) => {
      const progress = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = parsed.number * eased;
      setDisplay(`${parsed.prefix}${current.toFixed(parsed.decimals)}${parsed.suffix}`);
      if (progress < 1) frame = requestAnimationFrame(tick);
    };
    frame = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(frame);
  }, [animated, parsed?.decimals, parsed?.number, parsed?.prefix, parsed?.suffix, value]);
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stat-value", children: display });
}
function useDebouncedDispatcher(dispatch, delayMs) {
  const latestDispatch = reactExports.useRef(dispatch);
  const timerRef = reactExports.useRef(null);
  const queuedValueRef = reactExports.useRef(null);
  reactExports.useEffect(() => {
    latestDispatch.current = dispatch;
  }, [dispatch]);
  reactExports.useEffect(() => {
    return () => {
      if (timerRef.current !== null) {
        window.clearTimeout(timerRef.current);
      }
    };
  }, []);
  const flush = reactExports.useCallback((explicitValue) => {
    const nextValue = explicitValue ?? queuedValueRef.current;
    if (timerRef.current !== null) {
      window.clearTimeout(timerRef.current);
      timerRef.current = null;
    }
    if (nextValue === null || nextValue === void 0) return;
    queuedValueRef.current = null;
    latestDispatch.current(nextValue);
  }, []);
  const schedule = reactExports.useCallback((value) => {
    queuedValueRef.current = value;
    if (delayMs <= 0) {
      flush(value);
      return;
    }
    if (timerRef.current !== null) {
      window.clearTimeout(timerRef.current);
    }
    timerRef.current = window.setTimeout(() => {
      const queued = queuedValueRef.current;
      queuedValueRef.current = null;
      timerRef.current = null;
      if (queued !== null && queued !== void 0) {
        latestDispatch.current(queued);
      }
    }, delayMs);
  }, [delayMs, flush]);
  return { flush, schedule };
}
function InputComponent({ props: p, dispatch }) {
  const incomingValue = String(p.value || "");
  const [value, setValue] = reactExports.useState(incomingValue);
  const localDirtyRef = reactExports.useRef(false);
  const lastDispatchedRef = reactExports.useRef(incomingValue);
  const inputType = String(p.inputType || "text");
  const changeStrategy = String(p.changeStrategy || (inputType === "number" || inputType === "date" ? "immediate" : "debounce"));
  const debounceMs = Math.max(0, Number(p.debounceMs ?? 180));
  const syncOnBlur = p.syncOnBlur !== false;
  const { flush, schedule } = useDebouncedDispatcher((nextValue) => {
    lastDispatchedRef.current = nextValue;
    dispatch(nextValue);
  }, debounceMs);
  reactExports.useEffect(() => {
    if (!localDirtyRef.current || incomingValue === lastDispatchedRef.current) {
      setValue(incomingValue);
      localDirtyRef.current = false;
    }
  }, [incomingValue]);
  const commitValue = reactExports.useCallback((nextValue, immediate = false) => {
    localDirtyRef.current = true;
    if (changeStrategy === "blur" && !immediate) return;
    if (immediate || changeStrategy === "immediate") flush(nextValue);
    else schedule(nextValue);
  }, [changeStrategy, flush, schedule]);
  const commonProps = {
    name: p.name,
    placeholder: p.placeholder || "",
    value,
    disabled: Boolean(p.disabled),
    "aria-busy": Boolean(p.loading),
    onChange: (event) => {
      const nextValue = event.target.value;
      setValue(nextValue);
      commitValue(nextValue);
    },
    onBlur: () => {
      if (syncOnBlur || changeStrategy === "blur") {
        flush(value);
      }
    }
  };
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-form-field"]), style: resolveMotionStyle(p), children: [
    p.label && /* @__PURE__ */ jsxRuntimeExports.jsx("label", { className: "bf-label", children: p.label }),
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-field-loading", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-sm" }) }) : null,
    inputType === "textarea" ? /* @__PURE__ */ jsxRuntimeExports.jsx("textarea", { ...commonProps, className: "bf-textarea" }) : /* @__PURE__ */ jsxRuntimeExports.jsx("input", { ...commonProps, className: `bf-input${p.error ? " error" : ""}`, type: inputType }),
    p.error && /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-input-error", children: p.error })
  ] });
}
function DateRangePickerComponent({ props: p, dispatch }) {
  const [start, setStart] = reactExports.useState(p.start || "");
  const [end, setEnd] = reactExports.useState(p.end || "");
  reactExports.useEffect(() => {
    setStart(p.start || "");
    setEnd(p.end || "");
  }, [p.start, p.end]);
  const emit = (nextStart, nextEnd) => dispatch({ start: nextStart, end: nextEnd });
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-form-field", p.loading ? "bf-is-loading" : ""]), style: resolveMotionStyle(p), children: [
    p.label && /* @__PURE__ */ jsxRuntimeExports.jsx("label", { className: "bf-label", children: p.label }),
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-field-loading", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-sm" }) }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-date-range", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx(
        "input",
        {
          className: "bf-input",
          type: "date",
          name: `${p.name}_start`,
          value: start,
          disabled: Boolean(p.disabled) || Boolean(p.loading),
          onChange: (e) => {
            const next = e.target.value;
            setStart(next);
            emit(next, end);
          }
        }
      ),
      /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-date-range-sep", children: "to" }),
      /* @__PURE__ */ jsxRuntimeExports.jsx(
        "input",
        {
          className: "bf-input",
          type: "date",
          name: `${p.name}_end`,
          value: end,
          disabled: Boolean(p.disabled) || Boolean(p.loading),
          onChange: (e) => {
            const next = e.target.value;
            setEnd(next);
            emit(start, next);
          }
        }
      )
    ] })
  ] });
}
function MultiSelectComponent({ props: p, dispatch }) {
  const incomingValues = (p.values || []).map(String);
  const [selectedValues, setSelectedValues] = reactExports.useState(incomingValues);
  const options = p.options || [];
  reactExports.useEffect(() => {
    setSelectedValues(incomingValues);
  }, [p.values]);
  const toggleValue = (value) => {
    const selected = new Set(selectedValues);
    if (selected.has(value)) selected.delete(value);
    else selected.add(value);
    const next = Array.from(selected);
    setSelectedValues(next);
    dispatch(next);
  };
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-form-field", p.loading ? "bf-is-loading" : ""]), style: resolveMotionStyle(p), children: [
    p.label && /* @__PURE__ */ jsxRuntimeExports.jsx("label", { className: "bf-label", children: p.label }),
    p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-field-loading", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-sm" }) }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-multiselect", children: [
      selectedValues.map((value) => /* @__PURE__ */ jsxRuntimeExports.jsx("input", { type: "hidden", name: p.name, value }, `hidden-${value}`)),
      !selectedValues.length && p.placeholder ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-multiselect-placeholder", children: p.placeholder }) : null,
      options.map((option) => {
        const active = selectedValues.includes(option.value);
        return /* @__PURE__ */ jsxRuntimeExports.jsx(
          "button",
          {
            type: "button",
            className: `bf-multiselect-chip ${active ? "active" : ""}`,
            disabled: Boolean(p.disabled) || Boolean(p.loading),
            onClick: () => toggleValue(option.value),
            children: option.label
          },
          option.value
        );
      })
    ] })
  ] });
}
function SidebarComponent({ props: p, children, ctx }) {
  const activePath = window.location.pathname;
  const [mobileOpen, setMobileOpen] = reactExports.useState(false);
  const closeSidebar = () => setMobileOpen(false);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs(jsxRuntimeExports.Fragment, { children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-mobile-nav", children: /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: "bf-mobile-nav-toggle", onClick: () => setMobileOpen((open) => !open), children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "LayoutDashboard", size: 16 }),
      /* @__PURE__ */ jsxRuntimeExports.jsxs("span", { className: "bf-mobile-nav-copy", children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("strong", { children: p.brandName }),
        p.tagline ? /* @__PURE__ */ jsxRuntimeExports.jsx("small", { children: p.tagline }) : null
      ] })
    ] }) }),
    mobileOpen ? /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-sidebar-backdrop", onClick: closeSidebar, "aria-label": "Close navigation" }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("aside", { className: `bf-sidebar ${mobileOpen ? "open" : ""}`, children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-sidebar-brand", children: [
        p.logo ? /* @__PURE__ */ jsxRuntimeExports.jsx("img", { src: p.logo, alt: "logo", width: 28, height: 28, style: { borderRadius: 6 } }) : /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-sidebar-brand-logo", children: (p.brandName || "B").charAt(0) }),
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-sidebar-brand-copy", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-sidebar-brand-name", children: p.brandName }),
          p.tagline ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-sidebar-brand-tagline", children: p.tagline }) : null
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-sidebar-close", onClick: closeSidebar, "aria-label": "Close navigation", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: "X", size: 16 }) })
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("nav", { className: "bf-nav-section", children: children.map((child, index) => {
        const cp = child.props;
        const isActive = activePath === cp.path;
        return /* @__PURE__ */ jsxRuntimeExports.jsxs(
          "button",
          {
            className: `bf-nav-item ${isActive ? "active" : ""}`,
            onClick: () => {
              closeSidebar();
              ctx.navigate(cp.path);
            },
            children: [
              cp.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-nav-icon", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: cp.icon, size: 16 }) }) : null,
              cp.label,
              cp.badge ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-nav-badge", children: cp.badge }) : null
            ]
          },
          `${cp.path}-${index}`
        );
      }) }),
      Boolean(p.showThemeToggle) ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-sidebar-footer", children: /* @__PURE__ */ jsxRuntimeExports.jsx(ThemeToggleComponent, { props: { label: "Theme", lightLabel: "Light", darkLabel: "Dark" }, ctx }) }) : null
    ] })
  ] });
}
function TopNavComponent({ props: p, children, ctx }) {
  const activePath = window.location.pathname;
  const [mobileOpen, setMobileOpen] = reactExports.useState(false);
  const actions = p.actions || [];
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("header", { className: `bf-topnav ${p.sticky !== false ? "sticky" : ""}`, children: [
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-topnav-inner", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-topnav-brand", children: [
        p.logo ? /* @__PURE__ */ jsxRuntimeExports.jsx("img", { className: "bf-topnav-logo", src: p.logo, alt: String(p.brandName || "Brand") }) : /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-sidebar-brand-logo", children: String(p.brandName || "B").charAt(0) }),
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-topnav-copy", children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-topnav-brand-name", children: p.brandName }),
          p.tagline ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-topnav-brand-tagline", children: p.tagline }) : null
        ] })
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("nav", { className: "bf-topnav-links", children: children.map((child, index) => {
        const cp = child.props;
        const isActive = activePath === cp.path;
        return /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: `bf-topnav-link ${isActive ? "active" : ""}`, onClick: () => ctx.navigate(cp.path), children: [
          cp.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: cp.icon, size: 14 }) : null,
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: cp.label }),
          cp.badge ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-nav-badge", children: cp.badge }) : null
        ] }, `${cp.path}-${index}`);
      }) }),
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-topnav-actions", children: [
        Boolean(p.showThemeToggle) ? /* @__PURE__ */ jsxRuntimeExports.jsx(ThemeToggleComponent, { props: { label: "Theme", lightLabel: "Light", darkLabel: "Dark" }, ctx }) : null,
        actions.length ? renderChildren(actions, ctx, "topnav-actions") : null,
        /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-topnav-menu", onClick: () => setMobileOpen((open) => !open), "aria-label": "Toggle navigation menu", children: /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: mobileOpen ? "X" : "LayoutDashboard", size: 16 }) })
      ] })
    ] }),
    mobileOpen ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-topnav-mobile", children: /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-topnav-mobile-panel", children: [
      children.map((child, index) => {
        const cp = child.props;
        const isActive = activePath === cp.path;
        return /* @__PURE__ */ jsxRuntimeExports.jsxs(
          "button",
          {
            type: "button",
            className: `bf-topnav-mobile-link ${isActive ? "active" : ""}`,
            onClick: () => {
              setMobileOpen(false);
              ctx.navigate(cp.path);
            },
            children: [
              cp.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: cp.icon, size: 15 }) : null,
              /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: cp.label }),
              cp.badge ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-nav-badge", children: cp.badge }) : null
            ]
          },
          `mobile-${cp.path}-${index}`
        );
      }),
      actions.length ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-topnav-mobile-actions", children: renderChildren(actions, ctx, "topnav-mobile-actions") }) : null
    ] }) }) : null
  ] });
}
function FormComponent({ props: p, children, ctx, nodeKey }) {
  const [submitting, setSubmitting] = reactExports.useState(false);
  const csrfToken = typeof document !== "undefined" ? document.cookie.split("; ").find((entry) => entry.startsWith("brickflowui_csrf="))?.split("=").slice(1).join("=") : void 0;
  return /* @__PURE__ */ jsxRuntimeExports.jsx(
    "form",
    {
      className: `bf-form ${submitting ? "bf-is-loading" : ""}`,
      onSubmit: async (e) => {
        e.preventDefault();
        setSubmitting(true);
        try {
          const data = {};
          new FormData(e.currentTarget).forEach((v, k) => {
            if (k in data) {
              const current = data[k];
              if (Array.isArray(current)) current.push(v);
              else data[k] = [current, v];
            } else {
              data[k] = v;
            }
          });
          const resp = await fetch(p.action, {
            method: p.method || "POST",
            credentials: "same-origin",
            headers: {
              "Content-Type": "application/json",
              ...csrfToken ? { "X-Brickflow-Csrf": decodeURIComponent(csrfToken) } : {}
            },
            body: JSON.stringify(data)
          });
          if (resp.ok && p.successRedirect) {
            if (p.reloadOnSuccess) {
              window.location.assign(p.successRedirect);
            } else {
              ctx.navigate(p.successRedirect);
            }
          }
        } finally {
          setSubmitting(false);
        }
      },
      children: /* @__PURE__ */ jsxRuntimeExports.jsx("fieldset", { className: "bf-form-fieldset", disabled: submitting, children: renderChildren(children, ctx, nodeKey) })
    }
  );
}
function AccordionComponent({ props: p, children, ctx, nodeKey }) {
  const defaultOpen = (p.defaultOpen || []).map(Number);
  const [openItems, setOpenItems] = reactExports.useState(defaultOpen);
  const allowMultiple = Boolean(p.allowMultiple);
  const toggle = (index) => {
    setOpenItems((prev) => {
      if (prev.includes(index)) return prev.filter((item) => item !== index);
      if (allowMultiple) return [...prev, index];
      return [index];
    });
  };
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-accordion", children: children.map((child, index) => {
    const cp = child.props;
    const open = openItems.includes(index);
    return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-accordion-item ${open ? "open" : ""}`, children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: "bf-accordion-trigger", onClick: () => toggle(index), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-accordion-trigger-main", children: [
          cp.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: cp.icon, size: 15 }) : null,
          /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { children: [
            /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-accordion-title", children: cp.title }),
            cp.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-accordion-subtitle", children: cp.subtitle }) : null
          ] })
        ] }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-accordion-chevron", children: open ? "−" : "+" })
      ] }),
      open ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-accordion-content", children: renderChildren(child.children, ctx, `${nodeKey}-accordion-${index}`) }) : null
    ] }, `${nodeKey}-${index}`);
  }) });
}
function SparklineStatComponent({ props: p }) {
  const color = p.color || "var(--db-primary)";
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-sparkline-stat", children: [
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-sparkline-header", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stat-label", children: p.label }),
      p.delta ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-stat-delta ${p.deltaType || "neutral"}`, children: p.delta }) : null
    ] }),
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stat-value", children: p.value }),
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-sparkline-chart", children: /* @__PURE__ */ jsxRuntimeExports.jsx(ResponsiveContainer, { width: "100%", height: 70, children: /* @__PURE__ */ jsxRuntimeExports.jsx(LineChart, { data: p.data || [], children: /* @__PURE__ */ jsxRuntimeExports.jsx(Line, { dataKey: p.yKey, stroke: color, strokeWidth: 2, dot: false }) }) }) })
  ] });
}
function GaugeChartComponent({ props: p }) {
  const min = Number(p.min ?? 0);
  const max = Number(p.max ?? 100);
  const value = Number(p.value ?? 0);
  const pct = Math.max(0, Math.min(1, (value - min) / Math.max(1, max - min)));
  const degrees = -90 + pct * 180;
  return chartShell(
    String(p.title || "gauge"),
    p,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-gauge", style: { minHeight: p.height || 220 }, children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-gauge-arc", children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-gauge-fill", style: { "--bf-gauge-pct": pct, background: p.color || "var(--db-primary)" } }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-gauge-needle", style: { transform: `rotate(${degrees}deg)` } })
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-gauge-value", children: value.toLocaleString() }),
      p.label ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-gauge-label", children: p.label }) : null
    ] })
  );
}
function HeatmapComponent({ props: p, dispatch }) {
  const data = p.data || [];
  if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No heatmap data available" });
  const xKey = p.xKey;
  const yKey = p.yKey;
  const valueKey = p.valueKey;
  const xs = Array.from(new Set(data.map((row) => String(row[xKey] ?? ""))));
  const ys = Array.from(new Set(data.map((row) => String(row[yKey] ?? ""))));
  const max = Math.max(1, ...data.map((row) => Number(row[valueKey] ?? 0)));
  const lookup = new Map(data.map((row) => [`${row[xKey]}::${row[yKey]}`, row]));
  return chartShell(
    "heatmap",
    p,
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-heatmap", style: { "--bf-heatmap-cols": xs.length + 1 }, children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-heatmap-corner" }),
      xs.map((x) => /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-heatmap-axis", children: x }, `x-${x}`)),
      ys.map((y) => /* @__PURE__ */ jsxRuntimeExports.jsxs(React.Fragment, { children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-heatmap-axis y", children: y }),
        xs.map((x) => {
          const row = lookup.get(`${x}::${y}`);
          const value = Number(row?.[valueKey] ?? 0);
          const alpha = Math.max(0.08, Math.min(0.9, value / max));
          return /* @__PURE__ */ jsxRuntimeExports.jsx(
            "button",
            {
              type: "button",
              className: "bf-heatmap-cell",
              title: `${x} / ${y}: ${value}`,
              style: { background: `color-mix(in srgb, ${p.color || "var(--db-primary)"} ${Math.round(alpha * 100)}%, var(--db-surface))` },
              onClick: () => row && dispatch(row),
              children: value
            },
            `${x}-${y}`
          );
        })
      ] }, `row-${y}`))
    ] })
  );
}
function PipelineGraphComponent({ props: p, dispatch }) {
  const nodes = p.nodes || [];
  const edges = p.edges || [];
  const vertical = p.layout === "top-to-bottom";
  if (!nodes.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-state", children: p.emptyMessage || "No pipeline nodes available" });
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-pipeline ${vertical ? "vertical" : "horizontal"} ${p.animated ? "animated" : ""}`, children: [
    p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chart-title", children: p.title }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-pipeline-canvas", children: nodes.map((node, index) => {
      const incoming = edges.filter((edge) => edge.to === node.id).length;
      const outgoing = edges.filter((edge) => edge.from === node.id).length;
      const tone = statusTone(node.status);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs(React.Fragment, { children: [
        /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: `bf-pipeline-node ${tone}`, onClick: () => dispatch(node), children: [
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-pipeline-node-layer", children: String(node.layer ?? node.type ?? "step") }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-pipeline-node-title", children: String(node.label ?? node.id ?? "") }),
          /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-pipeline-node-meta", children: String(node.status ?? "unknown") }),
          /* @__PURE__ */ jsxRuntimeExports.jsxs("span", { className: "bf-pipeline-node-flow", children: [
            incoming,
            " in / ",
            outgoing,
            " out"
          ] })
        ] }),
        index < nodes.length - 1 ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-pipeline-edge ${p.animated ? "pulse" : ""}` }) : null
      ] }, String(node.id ?? index));
    }) })
  ] });
}
function StatusStripComponent({ props: p }) {
  const items = p.items || [];
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-status-strip"]), style: resolveMotionStyle(p), children: [
    p.title ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-card-title", children: p.title }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-status-strip-grid", style: { "--bf-status-cols": Number(p.columns || 4) }, children: items.map((item, index) => {
      const tone = statusTone(item.status || item.tone);
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-signal-card ${tone}`, children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-signal-label", children: String(item.label ?? "") }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-signal-value", children: String(item.value ?? "") }),
        item.detail ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-signal-detail", children: String(item.detail) }) : null
      ] }, index);
    }) })
  ] });
}
function StepperComponent({ props: p }) {
  const steps = p.steps || [];
  const active = Number(p.active || 0);
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: resolveMotionClass(p, [`bf-stepper`, `bf-stepper-${p.orientation || "horizontal"}`]), style: resolveMotionStyle(p), children: steps.map((step, index) => {
    const state = index < active ? "complete" : index === active ? "active" : "pending";
    return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-stepper-step ${state}`, children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stepper-dot", children: index + 1 }),
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stepper-title", children: String(step.label ?? step.title ?? "") }),
        step.description ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-stepper-description", children: String(step.description) }) : null
      ] })
    ] }, index);
  }) });
}
function KanbanBoardComponent({ props: p, dispatch }) {
  const columns = p.columns || [];
  return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: resolveMotionClass(p, ["bf-kanban"]), style: resolveMotionStyle(p), children: columns.map((column, columnIndex) => {
    const cards = column.cards || [];
    return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-kanban-column", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-kanban-header", children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: String(column.label ?? column.title ?? "") }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-kanban-count", children: cards.length })
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-kanban-cards", children: cards.map((card, cardIndex) => /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: `bf-kanban-card ${statusTone(card.status)}`, onClick: () => dispatch({ ...card, column: column.id ?? column.label }), children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-kanban-card-title", children: String(card.title ?? "") }),
        card.subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-kanban-card-subtitle", children: String(card.subtitle) }) : null,
        card.status ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-kanban-card-status", children: String(card.status) }) : null
      ] }, String(card.id ?? cardIndex))) })
    ] }, String(column.id ?? columnIndex));
  }) });
}
function ChatMessageComponent({ props: p }) {
  const role = p.role || "assistant";
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, [`bf-chat-message`, role, statusTone(p.tone)]), style: resolveMotionStyle(p), children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chat-avatar", children: p.avatar ? String(p.avatar) : role.slice(0, 1).toUpperCase() }),
    /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chat-bubble", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-chat-meta", children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: String(p.name ?? role) }),
        p.timestamp ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: String(p.timestamp) }) : null
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-chat-content", children: String(p.content ?? "") })
    ] })
  ] });
}
function ChatInputComponent({ props: p, dispatchChange, dispatchSubmit }) {
  const incomingValue = String(p.value || "");
  const [value, setValue] = reactExports.useState(incomingValue);
  const localDirtyRef = reactExports.useRef(false);
  const lastDispatchedRef = reactExports.useRef(incomingValue);
  const changeStrategy = String(p.changeStrategy || "debounce");
  const debounceMs = Math.max(0, Number(p.debounceMs ?? 180));
  const { flush, schedule } = useDebouncedDispatcher((nextValue) => {
    lastDispatchedRef.current = nextValue;
    dispatchChange(nextValue);
  }, debounceMs);
  reactExports.useEffect(() => {
    if (!localDirtyRef.current || incomingValue === lastDispatchedRef.current) {
      setValue(incomingValue);
      localDirtyRef.current = false;
    }
  }, [incomingValue]);
  const commitValue = reactExports.useCallback((nextValue, immediate = false) => {
    localDirtyRef.current = true;
    if (changeStrategy === "blur" && !immediate) return;
    if (immediate || changeStrategy === "immediate") flush(nextValue);
    else schedule(nextValue);
  }, [changeStrategy, flush, schedule]);
  const submit = () => {
    const next = value.trim();
    if (!next || p.disabled || p.loading) return;
    flush(value);
    dispatchSubmit(next);
  };
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-chat-input"]), style: resolveMotionStyle(p), children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx(
      "input",
      {
        className: "bf-input",
        name: p.name || "message",
        value,
        placeholder: p.placeholder || "Ask a question",
        disabled: Boolean(p.disabled),
        onChange: (event) => {
          const nextValue = event.target.value;
          setValue(nextValue);
          commitValue(nextValue);
        },
        onBlur: () => flush(value),
        onKeyDown: (event) => {
          if (event.key === "Enter") submit();
        }
      }
    ),
    /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { type: "button", className: "bf-btn bf-btn-primary", disabled: Boolean(p.disabled) || Boolean(p.loading) || !value.trim(), onClick: submit, children: [
      p.loading ? /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-spinner bf-spinner-sm" }) : null,
      p.submitLabel || "Send"
    ] })
  ] });
}
function tableCellTone(row, col, fallback) {
  const keyedTone = col.toneKey ? row[String(col.toneKey)] : void 0;
  return statusTone(keyedTone ?? fallback ?? col.color);
}
function renderTableCell(row, col) {
  const rawValue = row[col.key];
  const format = String(col.format || "text");
  if (format === "badge" || format === "status") {
    const tone = tableCellTone(row, col, rawValue);
    return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: `bf-table-pill ${tone}`, children: String(rawValue ?? "") });
  }
  if (format === "progress") {
    const value = Number(rawValue ?? 0);
    const max = Number(col.max ?? 100);
    const pct = Math.max(0, Math.min(100, value / Math.max(1, max) * 100));
    return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-table-progress", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-table-progress-track", children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-table-progress-fill ${tableCellTone(row, col, rawValue)}`, style: { width: `${pct}%` } }) }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-table-progress-value", children: String(col.suffix ? `${value}${col.suffix}` : value) })
    ] });
  }
  if (format === "currency") {
    const value = Number(rawValue ?? 0);
    return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { children: new Intl.NumberFormat(void 0, { style: "currency", currency: String(col.currency || "USD"), maximumFractionDigits: 0 }).format(value) });
  }
  if (format === "metric") {
    return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-table-metric", children: String(rawValue ?? "") });
  }
  if (format === "image" || format === "avatar") {
    const src = String(rawValue ?? "");
    if (!src) return /* @__PURE__ */ jsxRuntimeExports.jsx("span", { className: "bf-table-empty-cell", children: "—" });
    return /* @__PURE__ */ jsxRuntimeExports.jsx(
      "img",
      {
        className: `bf-table-media ${format === "avatar" ? "avatar" : ""}`,
        src,
        alt: String(col.alt || col.label || "media")
      }
    );
  }
  return String(rawValue ?? "");
}
function TableComponent({ props: p, dispatch }) {
  const data = p.data || [];
  const columns = p.columns || [];
  const pageSize = p.pagination || 20;
  const [page, setPage] = reactExports.useState(0);
  const [sortKey, setSortKey] = reactExports.useState(null);
  const [sortDir, setSortDir] = reactExports.useState("asc");
  let sorted = [...data];
  if (sortKey) {
    sorted.sort((a, b) => {
      const av = String(a[sortKey] ?? "");
      const bv = String(b[sortKey] ?? "");
      return sortDir === "asc" ? av.localeCompare(bv, void 0, { numeric: true }) : bv.localeCompare(av, void 0, { numeric: true });
    });
  }
  const totalPages = Math.ceil(sorted.length / pageSize);
  const pageData = sorted.slice(page * pageSize, (page + 1) * pageSize);
  const handleSort = (key) => {
    if (sortKey === key) setSortDir((d) => d === "asc" ? "desc" : "asc");
    else {
      setSortKey(key);
      setSortDir("asc");
    }
    setPage(0);
  };
  const exportCsv = () => {
    const header = columns.map((col) => col.label).join(",");
    const rows = sorted.map(
      (row) => columns.map((col) => {
        const raw = String(row[col.key] ?? "");
        return `"${raw.split('"').join('""')}"`;
      }).join(",")
    );
    const csv = [header, ...rows].join("\n");
    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "brickflowui-table-export.csv";
    link.click();
    URL.revokeObjectURL(url);
  };
  if (p.loading) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { style: { display: "flex", justifyContent: "center", padding: 40 }, children: /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-spinner bf-spinner-lg" }) });
  if (p.errorMessage) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-table-empty", children: p.errorMessage });
  if (!data.length) return /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-table-empty", children: p.emptyMessage || "No data" });
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { children: [
    p.exportable && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-table-toolbar", children: /* @__PURE__ */ jsxRuntimeExports.jsx("button", { type: "button", className: "bf-btn bf-btn-secondary", style: { padding: "6px 12px", fontSize: 12 }, onClick: exportCsv, children: "Export CSV" }) }),
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-table-wrapper", children: /* @__PURE__ */ jsxRuntimeExports.jsxs("table", { className: "bf-table", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsx("thead", { children: /* @__PURE__ */ jsxRuntimeExports.jsx("tr", { children: columns.map((col) => /* @__PURE__ */ jsxRuntimeExports.jsxs("th", { onClick: () => col.sortable && handleSort(col.key), children: [
        col.label,
        col.sortable && sortKey === col.key && (sortDir === "asc" ? " ▲" : " ▼")
      ] }, col.key)) }) }),
      /* @__PURE__ */ jsxRuntimeExports.jsx("tbody", { children: pageData.map((row, ri) => {
        const rowClickId = p.rowClick;
        return /* @__PURE__ */ jsxRuntimeExports.jsx("tr", { className: rowClickId ? "clickable" : "", onClick: () => rowClickId && dispatch(rowClickId, { row }), children: columns.map((col) => /* @__PURE__ */ jsxRuntimeExports.jsx("td", { title: String(row[col.key] ?? ""), className: col.align ? `bf-table-align-${String(col.align)}` : "", children: renderTableCell(row, col) }, col.key)) }, ri);
      }) })
    ] }) }),
    totalPages > 1 && /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-table-pagination", children: [
      /* @__PURE__ */ jsxRuntimeExports.jsxs("span", { children: [
        "Showing ",
        page * pageSize + 1,
        "–",
        Math.min((page + 1) * pageSize, data.length),
        " of ",
        data.length
      ] }),
      /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-table-pagination-controls", children: [
        /* @__PURE__ */ jsxRuntimeExports.jsx("button", { className: "bf-btn bf-btn-secondary", style: { padding: "4px 10px", fontSize: 12 }, disabled: page === 0, onClick: () => setPage((p2) => p2 - 1), children: "← Prev" }),
        /* @__PURE__ */ jsxRuntimeExports.jsx("button", { className: "bf-btn bf-btn-secondary", style: { padding: "4px 10px", fontSize: 12 }, disabled: page >= totalPages - 1, onClick: () => setPage((p2) => p2 + 1), children: "Next →" })
      ] })
    ] })
  ] });
}
function TabsComponent({ props: p, children, ctx, nodeKey, dispatch }) {
  const [active, setActive] = reactExports.useState(p.defaultActive || 0);
  reactExports.useEffect(() => {
    setActive(p.defaultActive || 0);
  }, [p.defaultActive]);
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: resolveMotionClass(p, ["bf-tabs"]), style: resolveMotionStyle(p), children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-tabs-list", children: children.map((child, i) => {
      const cp = child.props;
      return /* @__PURE__ */ jsxRuntimeExports.jsxs("button", { className: `bf-tab-trigger ${active === i ? "active" : ""}`, onClick: () => {
        setActive(i);
        const changeId = p.change;
        if (changeId) dispatch(changeId, { index: i });
      }, children: [
        cp.icon ? /* @__PURE__ */ jsxRuntimeExports.jsx(Icon, { name: cp.icon, size: 14 }) : null,
        cp.label
      ] }, i);
    }) }),
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-tab-content", children: children[active]?.children && renderChildren(children[active].children, ctx, `${nodeKey}-tab-${active}`) })
  ] });
}
const LOADING_BOOTSTRAP = window.__BRICKFLOW_BOOTSTRAP__ || {};
function resolveLoadingConfig(mode) {
  const modeOverrides = LOADING_BOOTSTRAP.modes?.[mode] || {};
  return {
    ...LOADING_BOOTSTRAP,
    ...modeOverrides
  };
}
function applyPatch(tree, patch) {
  const { op, path, node, props } = patch;
  if (path.length === 0) {
    if (op === "replace" && node) return node;
    if (op === "update_props" && props) {
      const nextProps = { ...tree.props };
      for (const [key, value] of Object.entries(props)) {
        if (value === null) delete nextProps[key];
        else nextProps[key] = value;
      }
      return { ...tree, props: nextProps };
    }
    return tree;
  }
  const [idx, ...rest] = path;
  const newChildren = [...tree.children];
  if (op === "remove" && rest.length === 0) {
    newChildren.splice(idx, 1);
    return { ...tree, children: newChildren };
  }
  if (op === "insert" && rest.length === 0 && node) {
    newChildren.splice(idx, 0, node);
    return { ...tree, children: newChildren };
  }
  if (idx < newChildren.length) {
    newChildren[idx] = applyPatch(newChildren[idx], { op, path: rest, node, props });
  } else if (op === "insert" && node) {
    newChildren.push(node);
  }
  return { ...tree, children: newChildren };
}
function LoadingVisual({ status, themeMode }) {
  const config = resolveLoadingConfig(themeMode);
  const asset = config.video || config.asset;
  const kind = config.video ? "video" : config.assetKind;
  const animation = config.animation || "spinner";
  const title = config.title || "BrickflowUI";
  const subtitle = config.subtitle;
  const message = status === "connecting" ? config.message || "Connecting to runtime..." : status === "disconnected" ? config.reconnectingMessage || "Reconnecting..." : status === "error" ? config.errorMessage || "Connection error - retrying..." : "Loading...";
  return /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: `bf-loading-screen bf-loading-${animation}`, children: [
    !config.textOnly ? kind === "video" && asset ? /* @__PURE__ */ jsxRuntimeExports.jsx(
      "video",
      {
        className: "bf-loading-media",
        src: asset,
        autoPlay: true,
        muted: true,
        loop: true,
        playsInline: true
      }
    ) : asset ? /* @__PURE__ */ jsxRuntimeExports.jsx("img", { className: "bf-loading-media", src: asset, alt: `${title} loading` }) : /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: `bf-spinner bf-spinner-lg ${animation === "pulse" ? "bf-spinner-pulse" : ""}` }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-loading-brand", children: title }),
    subtitle ? /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-loading-subtitle", children: subtitle }) : null,
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-loading-hint", children: message })
  ] });
}
function resolveInitialThemeMode() {
  const bootstrapMode = LOADING_BOOTSTRAP.themeMode === "dark" ? "dark" : "light";
  try {
    const stored = window.localStorage.getItem("brickflowui.theme");
    return stored === "light" || stored === "dark" ? stored : bootstrapMode;
  } catch {
    return bootstrapMode;
  }
}
function resolveInitialStylePreset() {
  return LOADING_BOOTSTRAP.stylePreset || "modern";
}
function App() {
  const [vdom, setVdom] = reactExports.useState(null);
  const [status, setStatus] = reactExports.useState("connecting");
  const [error, setError] = reactExports.useState(null);
  const [pendingEvents, setPendingEvents] = reactExports.useState(/* @__PURE__ */ new Map());
  const [themeMode, setThemeModeState] = reactExports.useState(resolveInitialThemeMode);
  const [stylePreset] = reactExports.useState(resolveInitialStylePreset);
  const wsRef = reactExports.useRef(null);
  const vdomRef = reactExports.useRef(null);
  const frameRef = reactExports.useRef(null);
  const queuedTreeRef = reactExports.useRef(null);
  const flushQueuedTree = reactExports.useCallback(() => {
    frameRef.current = null;
    const nextTree = queuedTreeRef.current;
    if (!nextTree) return;
    queuedTreeRef.current = null;
    reactExports.startTransition(() => {
      setVdom(nextTree);
    });
  }, []);
  const scheduleTreeCommit = reactExports.useCallback((nextTree) => {
    queuedTreeRef.current = nextTree;
    if (frameRef.current !== null) return;
    frameRef.current = window.requestAnimationFrame(flushQueuedTree);
  }, [flushQueuedTree]);
  const dispatch = reactExports.useCallback((event_id, data = {}) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      setPendingEvents((prev) => {
        const next = new Map(prev);
        next.set(event_id, (next.get(event_id) || 0) + 1);
        return next;
      });
      wsRef.current.send(JSON.stringify({ type: "event", event_id, data }));
    }
  }, []);
  const setThemeMode = reactExports.useCallback((mode) => {
    setThemeModeState(mode);
    document.documentElement.dataset.themeMode = mode;
    try {
      window.localStorage.setItem("brickflowui.theme", mode);
    } catch {
    }
  }, []);
  const navigate = reactExports.useCallback((path) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ type: "navigate", path }));
      window.history.pushState({}, "", path);
    }
  }, []);
  reactExports.useEffect(() => {
    document.documentElement.dataset.themeMode = themeMode;
  }, [themeMode]);
  reactExports.useEffect(() => {
    document.documentElement.dataset.uiPreset = stylePreset;
  }, [stylePreset]);
  reactExports.useEffect(() => {
    let reconnectTimer;
    function connect() {
      const proto = location.protocol === "https:" ? "wss" : "ws";
      const ws = new WebSocket(`${proto}://${location.host}/events?path=${encodeURIComponent(window.location.pathname)}`);
      wsRef.current = ws;
      setStatus("connecting");
      ws.onopen = () => {
        setStatus("connected");
        setError(null);
      };
      ws.onmessage = (e) => {
        try {
          const msg = JSON.parse(e.data);
          if (msg.type === "full") {
            vdomRef.current = msg.tree;
            scheduleTreeCommit(msg.tree);
          } else if (msg.type === "patch") {
            if (vdomRef.current) {
              let updated = vdomRef.current;
              for (const patch of msg.patches) {
                updated = applyPatch(updated, patch);
              }
              vdomRef.current = updated;
              scheduleTreeCommit({ ...updated });
            }
          } else if (msg.type === "event_complete") {
            setPendingEvents((prev) => {
              const current = prev.get(msg.event_id);
              if (!current) return prev;
              const next = new Map(prev);
              if (current <= 1) next.delete(msg.event_id);
              else next.set(msg.event_id, current - 1);
              return next;
            });
          } else if (msg.type === "error") {
            setError(msg.message);
          }
        } catch (err) {
          console.error("[BrickflowUI] Failed to parse server message", err);
        }
      };
      ws.onclose = () => {
        setStatus("disconnected");
        setPendingEvents(/* @__PURE__ */ new Map());
        reconnectTimer = setTimeout(connect, 2500);
      };
      ws.onerror = () => {
        setStatus("error");
        setPendingEvents(/* @__PURE__ */ new Map());
        ws.close();
      };
    }
    connect();
    const handlePopstate = () => navigate(window.location.pathname);
    window.addEventListener("popstate", handlePopstate);
    return () => {
      clearTimeout(reconnectTimer);
      if (frameRef.current !== null) {
        window.cancelAnimationFrame(frameRef.current);
      }
      wsRef.current?.close();
      window.removeEventListener("popstate", handlePopstate);
    };
  }, [navigate, scheduleTreeCommit]);
  if (!vdom) {
    return /* @__PURE__ */ jsxRuntimeExports.jsx(LoadingVisual, { status, themeMode });
  }
  return /* @__PURE__ */ jsxRuntimeExports.jsxs(jsxRuntimeExports.Fragment, { children: [
    /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-page-shell", children: /* @__PURE__ */ jsxRuntimeExports.jsx(
      Renderer,
      {
        node: vdom,
        dispatch,
        navigate,
        pendingEvents,
        themeMode,
        setThemeMode
      }
    ) }),
    status === "disconnected" && /* @__PURE__ */ jsxRuntimeExports.jsx("div", { className: "bf-connection-banner", children: "Reconnecting to server..." }),
    error && /* @__PURE__ */ jsxRuntimeExports.jsxs("div", { className: "bf-connection-banner", style: { borderColor: "var(--db-error)", color: "var(--db-error)", background: "var(--db-error-bg)" }, children: [
      "Runtime error: ",
      error
    ] })
  ] });
}
ReactDOM.createRoot(document.getElementById("root")).render(
  /* @__PURE__ */ jsxRuntimeExports.jsx(React.StrictMode, { children: /* @__PURE__ */ jsxRuntimeExports.jsx(App, {}) })
);
//# sourceMappingURL=index-C210lFNz.js.map
