// i18n:managed-catalog — bilingual/regional catalog; UI via ar.csv
frappe.pages["user-academy"].on_page_load = function (wrapper) {
	const page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __("User Academy"),
		single_column: true,
	});
	page.body.addClass("no-border").html(`
<div class="container-fluid" style="max-width: 56rem; padding: 1.5rem 1rem;">
	<div class="frappe-card p-4">
		<h3 class="mb-3">${__("ErpGenEx User Academy")}</h3>
		<p class="text-muted mb-4">
			${__(
				"Free in-app learning for end users — no extra license. Use the links below and your organisation’s official guides."
			)}
		</p>
		<hr class="my-4" />
		<p class="mb-2"><strong>${__("Arabic")}</strong></p>
		<p class="text-muted" style="line-height: 1.6;">
			أكاديمية المستخدم: محتوى تعليمي داخل النظام لمساعدتك على استخدام الواجهات والخطوات الأساسية.
			راجع أيضًا توثيق منظمتك الرسمي ومسارات التدريب إن وُجدت.
		</p>
		<hr class="my-4" />
		<ul class="list-unstyled">
			<li class="mb-2">
				<a href="/app/List/Help%20Article/List" class="text-primary">${__("Help Articles")}</a>
			</li>
			<li class="mb-2">
				<a href="https://docs.frappe.io/framework/user/en" target="_blank" rel="noopener noreferrer" class="text-primary">${__(
					"Frappe user documentation (English)"
				)}</a>
			</li>
		</ul>
		<p class="text-muted small mt-4 mb-0">
			${__("Tip: press / on the desk to search, or use the Awesome Bar to jump to any DocType.")}
		</p>
	</div>
</div>
	`);
};
