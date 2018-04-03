.PHONY: code nginx

code:
	@cd ansible && \
	ansible-playbook site.yml -i ComPiLED, -t code

nginx:
	@cd ansible && \
	ansible-playbook site.yml -i ComPiLED, -t nginx --ask-vault-pass
